#!/usr/bin/env python
import tf
import rospy
import sys
import math
import numpy as np
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import Transform, Vector3, Twist
import exp_quat_func as eqf

def callback(message):
    ar_tag = message.transforms[0].child_frame_id
    if (ar_tag == ar_tag1 or ar_tag == ar_tag2 or ar_tag == ar_tag3 or ar_tag == ar_tag4):
        global newmessage
        global prev_ar_tag
        global prev_position
        global prev_theta

        # logic stuff 
        transform = message.transforms[0].transform
        translation = transform.translation
        rotation = transform.rotation
        quaternion = np.array([rotation.x, rotation.y,rotation.z, rotation.w])
        omega, theta = eqf.quaternion_to_exp(quaternion)
        translation = np.array([translation.x, translation.y, translation.z])
        g = eqf.create_rbt(omega, theta, translation)
        g_inv = eqf.inverse_g(g)

        if (ar_tag == ar_tag1): # picked up tag at (1,0)
            g_0A = np.array([[1, 0, 0, l1], [0, 0, 1, 0], [0, -1, 0, 0], [0, 0, 0, 1]])   
        elif (ar_tag == ar_tag2): # picked up tag at (0,1)
            g_0A = np.array([[0, 0, 1, 0], [-1, 0, 0, l2], [0, -1, 0, 0], [0, 0, 0, 1]])
        elif (ar_tag == ar_tag3): # picked up tag at (2,1)
            g_0A = np.array([[0, 0, -1, l1*2], [1, 0, 0, l2], [0, -1, 0, 0], [0, 0, 0, 1]])
        elif (ar_tag == ar_tag4): # picked up tag at (1,2)
            g_0A = np.array([[-1, 0, 0, l1], [0, 0, -1, l2*2], [0, -1, 0, 0], [0, 0, 0, 1]])

        position = np.dot(g_0A, g_inv)
        #print(ar_tag)
        #print(position)
        ZumyPosition = position[0:3, 3]
        # update 
        newmessage = True
        prev_ar_tag = ar_tag
        prev_position = ZumyPosition
        print(prev_position)
        prev_theta = theta


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

def rotateToDesiredTheta(x1, y1, x2, y2, desired_theta, curr_theta):
    print("desired theta: " + str(desired_theta) + " current theta: " + str(curr_theta))
    bound = 18
    upperbound = desired_theta + np.pi/bound
    lowerbound = desired_theta - np.pi/bound
   # print("here")
    twist.linear.x = 0
    """
    if(curr_theta < lowerbound):
        #print("publish twist")
        twist.angular.z = -0.2
    elif(curr_theta > upperbound):
        twist.angular.z = 0.2
"""
    if(curr_theta < lowerbound or curr_theta > upperbound):
        #print("publish twist")
        twist.angular.z = 0.2
        return False
    else:
        twist.angular.z = 0
        return True

def forward(x1, y1, x2, y2):
    twist.angular.z = 0
    bound = 0.10
    deltax = abs(x2-x1)
    deltay = abs(y2-y1)
    print("deltax: " + str(deltax) + " deltay:" + str(deltay))
    if (deltax > 0.10 or  deltay > 0.10):
        twist.linear.x = 0.15
    else:
        twist.linear.x = 0

def listener():
    # tf listener
    rospy.Subscriber("tf", TFMessage, callback)
    rospy.spin()

#Python's syntax for a main() method
if __name__ == '__main__':
    if len(sys.argv) < 6:
        print("Use: position_tracker.py zumy## [AR tag at (1.05, 0)] [AR tag at (0,0.91)] [AR tag at (2*1.05,0.91)] [AR tag at (1.05, 2*0.91)]  x y")
        sys.exit()


    # update these    
    newmessage = False
    prev_ar_tag = None
    prev_position = None
    prev_theta = None

    # parameters
    l1 = 1.05
    l2 = 0.91

    zumy = sys.argv[1]
    zumy_cmd = zumy + "/cmd_vel"
    ar_tag1 = 'ar_marker_' + sys.argv[2]
    ar_tag2 = 'ar_marker_' + sys.argv[3]
    ar_tag3 = 'ar_marker_' + sys.argv[4]
    ar_tag4 = 'ar_marker_' + sys.argv[5]
    x_des = float(sys.argv[6])
    y_des = float(sys.argv[7])
    twist = Twist()

    # zumy cmd_vel publisher node
    rospy.init_node('zumy_cmd')
    pub = rospy.Publisher(zumy_cmd, Twist, queue_size=2)
    rate = rospy.Rate(10)

    listener()

    twist.linear.y = 0
    twist.linear.z = 0
    twist.angular.x = 0
    twist.angular.y = 0

    #Check
    facingCorrectWay = False
    print (prev_position)
    while(prev_position == None):
        #print (prev_position)
        twist.linear.x = 0
        twist.angular.z = 0.2
        pub.publish(twist)
        #print (prev_position)

    print("here")
    while not rospy.is_shutdown():
        print("inside while loop")
        if (newmessage == True):
            des_theta = findDesiredTheta(prev_position[0], prev_position[1], x_des, y_des, prev_theta, prev_ar_tag)
            newmessage = False
            #rotateToDesiredTheta(x1, y1, x2, y2, theta, curr_theta)
        #else:
            """
            does not see an AR tag - do more than rotate
            case 1: rotate to look for an AR tag -> positionInitialized
            case 2: rotated off looking from an AR tag -> should call orientationEstimate
            """
            #twist.linear.x = 0
            #twist.angular.z = 0.2
        # function calls + modifying twists
        
        facingCorrectWay = rotateToDesiredTheta(prev_position[0], prev_position[1], x_des, y_des, des_theta, prev_theta)

        if (facingCorrectWay):
            forward(prev_position[0], prev_position[1], x_des, y_des)
        ## CHeck
        # if(curr_theta < lowerbound or curr_theta > upperbound):
        #     facingCorrectWay = False
        #     #Keep rotating
        # else:
        #     facingCorrectWay = True
        #     #GO FORWARD if it needs to move


        pub.publish(twist)
