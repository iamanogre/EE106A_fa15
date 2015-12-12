#!/usr/bin/env python

import sys
import rospy
from tfservice.srv import *
import math
import numpy as np
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import Transform, Vector3, Twist
from std_msgs.msg import Float32MultiArray
import exp_quat_func as eqf


def findDesiredTheta(x1, y1, x2, y2, curr_theta, ar_tag):
    """ 
    Calculates the theta [function of ar_tag] to face x2, y2. 
    x1, y1 - zumy ; x2, y2 - desired 
    """
    #print("x1: "+str(x1)+" x2: "+str(x2)+"\n"+"y1: "+str(y1)+" y2: "+str(y2))
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

def findDesiredTheta2(x1, y1, x2, y2):
    """ 
    Calculates the theta [function of ar_tag] to face x2, y2. 
    x1, y1 - zumy ; x2, y2 - desired 
    """
    #print("x1: "+str(x1)+" x2: "+str(x2)+"\n"+"y1: "+str(y1)+" y2: "+str(y2))
    deltax = abs(x2-x1)
    deltay = abs(y2-y1)
    psi = 0
    if (x2 > x1):
        if (y2 < y1):
            psi = np.pi + np.arctan(deltax/deltay)
        else:
            psi = np.pi * 3/2 + np.arctan(deltay/deltax)
    elif (x2 < x1):
        if (y2 < y1):
            psi = np.pi/2 + np.arctan(deltay/deltax)
        else:
            psi = np.arctan(deltax/deltay)

    #Returns absolute angle which the Zumy should be facing
    return psi

def isFacingDesTheta(desired_theta, curr_theta):
    #print("desired theta: " + str(desired_theta*180/np.pi) + " current theta: " + str(curr_theta*180/np.pi))

    if (curr_theta > desired_theta):
        if ((curr_theta  - desired_theta) > np.pi):
            return -1
        else: 
            return 1
    else:
        if ((desired_theta - curr_theta) > np.pi):
            return 1
        else:
            return -1

    # old
    # bound = 25
    # upperbound = (desired_theta + np.pi/bound) 
    # lowerbound = (desired_theta - np.pi/bound)
    # if(curr_theta < lowerbound):
    #     #print("curr_theta < lowerbound")
    #     return -1
    # elif (curr_theta > upperbound):
    #     #print("curr_theta > upperbound")
    #     return 1
    # else:
    #     return 0

def WithinLargeAngleBound(des_theta, curr_theta):
    #Returns true if it's within the specifed angle bound

    #In radians... and must be less than 180 degrees..
    # bound = (22*np.pi/180)
    bound = (18*np.pi/180)

    #Sets the upper and lower bounds
    upperbound = des_theta + bound
    lowerbound = des_theta - bound

    wrapped = False
    #Ensures the bounds are within 0-360 degrees
    if upperbound > 2*np.pi:
        upperbound = upperbound - 2*np.pi
        wrapped = True
    if lowerbound < 0:
        lowerbound = 2*np.pi + lowerbound
        wrapped = True

    #Determines if it's within the bound
    if (wrapped):
        if(curr_theta > lowerbound or curr_theta < lowerbound):
            return True
        else:
            return False
    else:
        if(curr_theta > lowerbound and curr_theta < upperbound):
            return True
        else:
            return False
    
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
    def __init__(self, mname, exploreService):
        self.mname = mname
        rospy.init_node(self.mname + '_zumy_cmd')
        
        # zumy3b/cmd_vel publisher
        zumy_cmd = self.mname + "/cmd_vel"
        self.pub = rospy.Publisher(zumy_cmd, Twist, queue_size=2)
        
        # explorer service
        self.exploreService = exploreService
          
        # twist to send to zumy
        self.twist = Twist()

        # position
        self.x = 0
        self.y = 0
        self.theta = 0
        self.getOrientation() # gets position

        self.x_des = 0
        self.y_des = 0

        self.finished = False

        # listen to zumy photo data
        self.photo_listen = rospy.Subscriber(self.mname + "/photo", Float32MultiArray, self.react)

        rospy.spin()

    # gets photo data
    def react(self, message):
        #print("in react right now")
        rospy.wait_for_service(self.exploreService)
        #print(message)
        try:
            service = rospy.ServiceProxy(self.exploreService, exploreSrv)
            response = service(self.mname, [self.x, self.y], message.data, self.finished)

            # gets position it should go to
            self.x_des = response.position[0]
            self.y_des = response.position[1]
            #print("desired position")
            self.run()

        except rospy.ServiceException, e:
            print "Service call failed: %s"%e
        #print(message)

    def getOrientation(self):
        ret = self.get_tf()
        if (ret.updated):
            #It see's an AR tag
            self.x = ret.position[0]
            self.y = ret.position[1]
            self.theta = ret.theta
        else:
            #It doesn't see an AR tag --> using global camera if available
            pos = self.get_global()
            if (pos.updated):
                self.x = pos.position[0]
                self.y = pos.position[1]
                self.theta = pos.theta
        if (self.theta > 0):
            print("successfully oriented")
        else: 
            print("did not orient")

    def run(self):
        """ main loop """

        #while not rospy.is_shutdown():
        ret = self.get_tf()
        self.finished = False

        # Assume no twist to be sent
        self.twist.linear.x = 0
        self.twist.linear.y = 0
        self.twist.linear.z = 0
        self.twist.angular.x = 0
        self.twist.angular.y = 0
        self.twist.angular.z = 0

        #Updates the position of the Zumy
        if (ret.updated):
            #It see's an AR tag
            self.x = ret.position[0]
            self.y = ret.position[1]
            self.theta = ret.theta
        else:
            #It doesn't see an AR tag --> using global camera if available
            pos = self.get_global()
            if (pos.updated):
                self.x = pos.position[0]
                self.y = pos.position[1]
                self.theta = pos.theta

        #Find the desired direction which it should be facing
        des_theta = findDesiredTheta2(self.x, self.y, self.x_des, self.y_des)


        # turn to face correct direction
        rotationDirection = isFacingDesTheta(des_theta, self.theta)
        facingCorrectWay = WithinLargeAngleBound(des_theta,self.theta)
        #print(facingCorrectWay)
        if (facingCorrectWay):
            forward = shouldGoForward(self.x, self.y, self.x_des, self.y_des)
            if (forward):
            #    print("go forward")
                self.twist.linear.x = 0.125#0.15 #Makes it go forward
                self.twist.angular.z = rotationDirection * 0.04#0.06 # Makes it rotate slightly as it's moving
            else:
                #Stop moving
                self.twist.linear.x = 0
                self.twist.angular.z = rotationDirection * 0
                self.finished = True

        else:
            #If not facing correct way then rotate in the appropriate direction
            self.twist.angular.z = rotationDirection * 0.18#0.21

        #Print out information
        print(str(self.finished) + "\tposition: " + str([self.x, self.y]) + "\ttheta: " + str(self.theta*180/np.pi) + "\tdesired " + str(des_theta*180/np.pi) + "\tdes_position: " + str([self.x_des, self.y_des]))

        # publish twist
        self.pub.publish(self.twist)
        #if (self.twist.angular.z != 0):s
        #    self.prev_twist.angular.z = self.twist.angular.z
        #print()
        """ # move towards goal and correct theta                


        else:
            #print("rotating to desired theta")
            #print(facingCorrectWay)
            self.twist.angular.z = facingCorrectWay * 0.2

        """
        #rospy.sleep(0.3)

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

    def get_global(self):
        """
        calls global_service server to get global position
        """
        rospy.wait_for_service('global_pos')
        try:
            service = rospy.ServiceProxy('global_pos', globalSrv)
            response = service()
            # may need to go back and change this to take in a zumy's tag number
            return response
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Use: position_tracker.py zumy## exploreService")
        sys.exit()

    # AR_tags
    ar_tag1 = 5 # [AR tag at (1.05, 0)]
    ar_tag2 = 6 # [AR tag at (0,0.91)] 
    ar_tag3 = 7 # [AR tag at (2*1.05,0.91)]
    ar_tag4 = 8 # [AR tag at (1.05, 2*0.91)]
    ar_tag_arr = [ar_tag1, ar_tag2, ar_tag3, ar_tag4]

    # user inputs --> put into tf_client class!
    zumy = sys.argv[1]
    exploreService = sys.argv[2]

    node = TF_client(zumy, exploreService)
    #node.run()

