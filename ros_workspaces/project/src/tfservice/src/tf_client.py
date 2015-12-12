#!/usr/bin/env python

import sys
import rospy
from tfservice.srv import *
from numpy.linalg import inv
import math
import numpy as np
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import Transform, Vector3, Twist
import exp_quat_func as eqf


def findDesiredTheta(x1, y1, x2, y2, curr_theta, ar_tag):
    """ 
    Calculates the theta [function of ar_tag] to face x2, y2. 
    x1, y1 - zumy ; x2, y2 - desired 
    """
    print("x1: "+str(x1)+" x2: "+str(x2)+"\n"+"y1: "+str(y1)+" y2: "+str(y2))
    deltax = abs(x2-x1)
    deltay = abs(y2-y1)
    if (x2 > x1):
        if (y2 < y1):
            psi = - np.arctan(deltax/deltay)
        else:
            psi = - np.pi/2 - np.arctan(deltay/deltax)
    elif (x2 < x1):
        if (y2 < y1):
            psi = np.arctan(deltax/deltay)
        else:
            psi = np.pi/2 + np.arctan(deltay/deltax)
    
    if (ar_tag == ar_tag1): # picked up tag at (1,0)
        rotate = np.pi
    elif (ar_tag == ar_tag2): # picked up tag at (0,1)
        rotate = np.pi + np.pi/2
    elif (ar_tag == ar_tag3): # picked up tag at (2,1)
        rotate = np.pi/2
    elif (ar_tag == ar_tag4): # picked up tag at (1,2)
        rotate = 0
    
    theta = - psi + rotate
    if (theta < 0):
        theta = theta + 2*np.pi
    return theta
   # print(theta * 180/np.pi)

def isFacingDesTheta(x1, y1, x2, y2, desired_theta, curr_theta):
    #print("desired theta: " + str(desired_theta) + " current theta: " + str(curr_theta))
    bound = 18
    upperbound = desired_theta + np.pi/bound
    lowerbound = desired_theta - np.pi/bound
    if(curr_theta < lowerbound):
        #print("curr_theta < lowerbound")
        return -1
    elif (curr_theta > upperbound):
        #print("curr_theta > upperbound")
        return 1
    else:
        return 0

def shouldGoForward(x1, y1, x2, y2):
    bound = 0.10
    deltax = abs(x2-x1)
    deltay = abs(y2-y1)
    #print("deltax: " + str(deltax) + " deltay:" + str(deltay))
    if (deltax > 0.10 or  deltay > 0.10):
        return True
    else:
        return False

class TF_client:
    def __init__(self, mname):
        rospy.init_node('zumy_cmd')
        # imu variables
        self.hertz = 10
        self.dt = 1./self.hertz
        self.rate = rospy.Rate(self.hertz)
        self.calTime = 5 # Calibration time in seconds
        self.initial_position_uncertainty = 0.10 # meters
        self.initial_orientation_uncertainty = 0.3 # radians (0.3rad ~ 15deg)
        self.camera_position_error = 0.05 # meters
        self.camera_orientation_error = 0.1 # radians (0.1rad ~ 5deg)
        self.C_lin = np.array([[1.,0.,0.,0.],[0.,0.,1.,0]]) # position camera measurement
        self.C_ang = 1. # orientation camera measurement
        self.G_lin = np.array([[0.5*pow(self.dt,2),self.dt,0.,0.],
                              [0.,0.,0.5*pow(self.dt,2),self.dt]]).T # position IMU input
        self.G_ang = self.dt # orientation IMU input
        self.A_lin = np.array([[1.,self.dt,0.,0.],[0.,1.,0.,0.],[0.,0.,1.,self.dt],[0.,0.,0.,1.]]) # translation dynamics
        self.A_ang = 1. # rotation dynamics
        self.updateFlag = True
        self.mname = mname

        # Measurement initialization -- only necessary temporarily while AR does not work
        self.u = None
        self.z = Transform()
            
        # zumy3b/cmd_vel publisher
        zumy_cmd = self.mname + "/cmd_vel"
        self.pub = rospy.Publisher(zumy_cmd, Twist, queue_size=2)
        
        #rate = rospy.Rate(10)    

        # twist to send to zumy
        self.prev_twist = Twist()
        self.twist = Twist()

        # position -> come back!
        # self.x = 0
        # self.y = 0

    def run(self):
        """ main loop """
        #r = rospy.Rate(5)
        self.prev_twist.linear.x = 0
        self.prev_twist.linear.y = 0
        self.prev_twist.linear.z = 0
        self.prev_twist.angular.x = 0
        self.prev_twist.angular.y = 0
        self.prev_twist.angular.z = 0.2

        # set default Q and mu values to eye(6) and zero
        Q = np.eye(6)
        mu = np.zeros(6)

        # Initial sensor calibration
        Q, mu = self.calibrateSensors()

        # Initialize Kalman filter
        self.P_lin = np.diag([1.,0.,1.,0.])*pow(self.initial_position_uncertainty,2)
        self.Q_lin = self.G_lin.dot(Q[:2,:2]).dot(self.G_lin.T)
        self.P_ang = pow(self.initial_orientation_uncertainty,2)
        self.Q_ang = self.G_ang*Q[5,5]*self.G_ang
        self.R_lin = np.eye(2)*self.camera_position_error
        self.R_ang = self.camera_orientation_error
        self.acc_bias = mu[:2]
        self.gyro_bias = mu[5]
        self.x_lin = np.array([self.z.translation.x, self.z.translation.y])
        self.v_lin = np.array([0.,0.])
        self.psi = 2*np.arccos(self.z.rotation.w)*np.sign(self.z.rotation.z) # Assume we have a quaternion with vertical axis

        while not rospy.is_shutdown():
            #Requests the position/orientation of the zumy (returns false + .. if unavailable)
            ret = self.get_tf()

            # Assume no twist to be sent
            self.twist.linear.x = 0
            self.twist.linear.y = 0
            self.twist.linear.z = 0
            self.twist.angular.x = 0
            self.twist.angular.y = 0
            self.twist.angular.z = 0

            #print(ret)
            #print(ret.theta*180/np.pi)
            #print(ret.rotation)

            rospy.wait_for_service('last_imu')
            try:
                get_imu = rospy.ServiceProxy('last_imu', ImuSrv)
                self.u = get_imu()
                print "Found IMU Update"
            except rospy.ServiceException, e:
                #print "Service call to IMU Server failed: %s"%e
                print "No IMU update this time step"
                # Assume previous measured u (Zero-Order Hold)

            self.timeUpdate(self.u) # **ESTIMATE POS FROM IMU ***
            if (ret.updated == True):
                self.z.translation.x = ret.position[0]
                self.z.translation.y = ret.position[1]
                self.z.translation.z = 0
                self.z.rotation = ret.rotation
                self.measurementUpdate(self.z) #**UPDATE CONCRETE POS**

            print(self.x_lin)
            # if (ret.updated == True):
            #     print("updated by ar tag")
            #     self.x_lin = np.array([ret.position[0],ret.position[1]])
            #     self.v_lin = np.array([0,0])
                #self.psi
            #print(self.x_lin)
            #print(self.v_lin)
                # self.measurementUpdate(self.z) **UPDATE CONCRETE POS**

            #print(ret)
            # if (ret.updated == True):
            #     # got updated information
            #     # print(ret.ar_tag)
            #     # find desired theta
            #     des_theta = findDesiredTheta(ret.position[0], ret.position[1], x_des, y_des, ret.theta, ret.ar_tag)
                
            #     # turn to face correct direction
            #     facingCorrectWay = isFacingDesTheta(ret.position[0], ret.position[1], x_des, y_des, des_theta, ret.theta)

            #     if (facingCorrectWay == 0):
            #         forward = shouldGoForward(ret.position[0], ret.position[1], x_des, y_des)
            #         if (forward):
            #             print("go forward")
            #             twist.linear.x = 0.15
            #     else:
            #         print("rotating to desired theta")
            #         print(facingCorrectWay)
            #         twist.angular.z = facingCorrectWay * 0.2

            # else:
            #     print("ret updated is false")
            #     # re-establish position - find another ar tag -> orientate
            #     # if (prev_twist.angular.z == 0):
            #     #     twist.angular.z = 0.2
            #     #     print("TEST")
            #     # else: 
            #     twist.angular.z = prev_twist.angular.z

            # # publish twist
            # print(twist.angular.z)
            # pub.publish(twist)
            # if (twist.angular.z != 0):
            #     prev_twist.angular.z = twist.angular.z

            rospy.sleep(0.3)

    def get_tf(self):
        """
        calls tf service server to get tf information
        """
        rospy.wait_for_service('last_tf')
        try:
            service = rospy.ServiceProxy('last_tf', tfSrv)
            response = service()
            #return response.new, response.tf
            return response
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e



    # data = true, update position and do stuff
    # data = false, start a timer and timer > 5 secs, look for new AR tag
    #               estimating position


    ##COPIED IN

    def calibrateSensors(self):
        startCal = rospy.get_rostime() # node time in seconds
        print "Starting sensor calibration..."
        m = np.empty([6,int(self.hertz*self.calTime)])
        for j in range(m.shape[1]):
            rospy.wait_for_service('last_imu')
            try:
                get_imu = rospy.ServiceProxy('last_imu', ImuSrv)
                u = get_imu()
                m[:,j] = [u.linear_acceleration.x,u.linear_acceleration.y,u.linear_acceleration.z,
                          u.angular_velocity.x, u.angular_velocity.y, u.angular_velocity.z]
            except rospy.ServiceException, e:
                #print "Service call to IMU Server failed: %s"%e
                print "No IMU update this time step"
                m[:,j] = np.zeros(6)  
            self.rate.sleep()
        endCal = rospy.get_rostime()
        print "Calibration complete. Took %f seconds"%(endCal-startCal).to_sec()
        Q = np.cov(m,bias=1)
        mu = np.mean(m,axis=1)
        print "Average accelerometer measurement: [%f, %f, %f]"%(mu[0], mu[1], mu[2])
        print "Accelerometer covariance matrix:"
        print Q[:3,:3]
        print "Average gyroscope measurement: [%f, %f, %f]"%(mu[3], mu[4], mu[5])
        print "Gyroscope covariance matrix:"
        print Q[3:,3:]
        return (Q,mu)

    # Compute the time update for every time step based on measured variations
    def timeUpdate(self,u):
        # Define inputs
        u_lin = np.array([u.linear_acceleration_filtered.x,u.linear_acceleration_filtered.y]) - self.acc_bias
        u_ang = u.angular_velocity_filtered.z - self.gyro_bias
        # Determine orientation
        rot = np.array([[np.cos(self.psi),-np.sin(self.psi)],[np.sin(self.psi),np.cos(self.psi)]])
        rotxv = np.kron(rot,np.eye(2))
        # Propagate dynamics
        self.x_lin += self.v_lin*self.dt + 0.5*rot.dot(u_lin)*pow(self.dt,2)
        self.v_lin += rot.dot(u_lin)*self.dt
        self.psi += u_ang*self.dt
        # Update uncertainty
        self.P_lin = self.A_lin.dot(self.P_lin).dot(self.A_lin.T)  \
                     + rotxv.dot(self.Q_lin).dot(rotxv.T)
        self.P_ang += self.Q_ang

      # Compute a measurement update based on the received information
    def measurementUpdate(self,z):
        # Compute innovation
        e_lin = np.array([z.translation.x, z.translation.y]) - self.x_lin
        e_ang = z.rotation.w - self.psi
        S_lin  = self.C_lin.dot(self.P_lin).dot(self.C_lin.T) + self.R_lin
        S_ang  = self.C_ang*self.P_ang*self.C_ang + self.R_ang
        # Compute Kalman gain
        K_lin = self.P_lin.dot(self.C_lin.T).dot(inv(S_lin))
        K_ang = self.P_ang*self.C_ang/S_ang
        # Update state
        xv = np.array([self.x_lin[0],self.v_lin[0],self.x_lin[1],self.v_lin[1]])
        xv += K_lin.dot(e_lin)
        self.x_lin = np.array([xv[0],xv[2]])
        self.v_lin = np.array([xv[1],xv[3]]) # np.array([0,0]) # 
        self.psi += K_ang*e_ang
        # Update uncertainty
        self.P_lin = (np.eye(4)-K_lin.dot(self.C_lin)).dot(self.P_lin)


if __name__ == "__main__":
    if len(sys.argv) != 8:
        print("Use: position_tracker.py zumy## [AR tag at (1.05, 0)] [AR tag at (0,0.91)] [AR tag at (2*1.05,0.91)] [AR tag at (1.05, 2*0.91)]  x y")
        sys.exit()

    # user inputs --> put into tf_client class!
    zumy = sys.argv[1]
    zumy_cmd = zumy + "/cmd_vel"
    ar_tag1 = sys.argv[2]
    ar_tag2 = sys.argv[3]
    ar_tag3 = sys.argv[4]
    ar_tag4 = sys.argv[5]
    ar_tag_arr = [ar_tag1, ar_tag2, ar_tag3, ar_tag4]
    x_des = float(sys.argv[6])
    y_des = float(sys.argv[7])

    node = TF_client(zumy)
    node.run()

