#!/usr/bin/env python
import tf
import rospy
import sys
import math
import numpy as np
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import Transform, Vector3, Twist
import exp_quat_func as eqf
import kin_func_skeleton as kfs

listener = None

def follow_ar_tag(zumy, ar_tags):

    # ar_tag = ar_tags['arZ']
    listener = tf.TransformListener()
    zumy_vel = rospy.Publisher('%s/cmd_vel' % zumy, Twist, queue_size=2)
    rate = rospy.Rate(10)
    #print ar_tags
    
    while not rospy.is_shutdown():
        try:
            (trans, rot) = listener.lookupTransform(ar_tags['arZ'], ar_tags['ar1'], rospy.Time(0))
            #(trans, rot) = listener.lookupTransform('ar_marker_5', 'ar_marker_3', rospy.Time(0))
        except:
            continue
        
        quaternion = np.array([rot[0], rot[1],rot[2], rot[3]])
        omega, theta = eqf.quaternion_to_exp(quaternion)
        translation = np.array([trans[0], trans[1], trans[2]])
        g_SZ = eqf.create_rbt(omega, theta, translation)

        position = g_SZ[0:3, 3]
        print("position: " + str(position))

        rotation = g_SZ[0:3, 0:3]
        omega, theta = eqf.find_omega_theta(rotation)  
        if(omega[2] < 0):
            theta = 2*np.pi - theta
        #print(omega)
        print(theta*180/np.pi)

        # when tried to use AR tag 6 with global camera
        # #print(rot)

        # #print(rot)
        # quaternion = np.array([rot[0], rot[1],rot[2], rot[3]])
        # omega, theta = eqf.quaternion_to_exp(quaternion)
        # translation = np.array([trans[0], trans[1], trans[2]])
        # g_SZ = eqf.create_rbt(omega, theta, translation)

        # #print(g_SZ[0:3, 0:3])
        # #print(kfs.rotation_3d(omega, theta))
        # l1 = 1.05
        # l2 = 0.91
        # g_0A = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        # #print(ar_tag)
        # #print(ar_tag_arr)
        # #Calculates the position of the zumy and orientation relative to the Origin
        # if (ar_tag == ar_tag_arr[0]): # picked up tag at (1,0)
        #     g_0A = np.array([[1, 0, 0, l1], [0, 0, 1, 0], [0, -1, 0, 0], [0, 0, 0, 1]])

        # elif (ar_tag == ar_tag_arr[1]): # picked up tag at (0,1)
        #     g_0A = np.array([[0, 0, 1, 0], [-1, 0, 0, l2], [0, -1, 0, 0], [0, 0, 0, 1]])
        # elif (ar_tag == ar_tag_arr[2]): # picked up tag at (2,1)
        #     g_0A = np.array([[0, 0, -1, l1*2], [1, 0, 0, l2], [0, -1, 0, 0], [0, 0, 0, 1]])

        #   #print(self.theta)
        # elif (ar_tag == ar_tag_arr[3]): # picked up tag at (1,2)
        #     g_0A = np.array([[-1, 0, 0, l1], [0, 0, -1, l2*2], [0, -1, 0, 0], [0, 0, 0, 1]])

        # position = np.dot(g_0A, g_SZ)

        # # get theta!
        # # maybe is not 90 degrees!!
        # g_rotateX = np.array([[1, 0, 0, 0], [0, 0, -1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
        # # g_rotateX = g_SZ
        # # g_rotateX[3, 0] = 0
        # # g_rotateX[3, 1] = 0
        # # g_rotateX[3, 2] = 0
        # print(g_rotateX)
        # #print(g_SZ)
        # #print(g_rotateX)
        # g_rotateX_inv = eqf.inverse_g(g_rotateX)
        # #print(g_rotateX_inv)
        # g_new = np.dot(g_rotateX_inv, g_SZ)
        # #print(g_new)
        # rotation = g_new[0:3, 0:3]
        # omega, theta = eqf.find_omega_theta(rotation)  


        # print(omega)
        # print(theta*180/np.pi)


        # # l1 = 1.05
        # # g_05 = np.array([[1, 0, 0, l1], [0, 0, 1, 0], [0, -1, 0, 0], [0, 0, 0, 1]])

        # #g = np.dot(g_0A, g_SZ)
        # position = position[0:3, 3]
        # #print(position)

        # # # find theta
        # # if(omega[1] < 0):
        # #   theta =  2*np.pi - theta
        
        # # true_theta = 2*np.pi - theta   
        # # true_theta  = 2*np.pi - true_theta

        # # print(true_theta*180/np.pi)

        # # YOUR CODE HERE
        # #  The code should compute the twist given 
        # #  the translation and rotation between arZ and ar1
        # #  Then send it publish it to the zumy
        # #print("trans: " + str(trans))
        
        # #(omega, theta) = eqf.quaternion_to_exp(rot)
        # #print("rot: "+ str(rot))
        # #print("omega: " + str(omega))
        # #print("theta: "+ str(theta*180/np.pi))

        # #quat = (eqf.exp_to_quaternion(omega, theta)).T
        # #print(quat)




if __name__=='__main__':    #print(q_3)
    #print(q)
    rospy.init_node('follow_ar_tag_twist')
    if len(sys.argv) < 4:
        print('Use: follow_ar_tag_manual.py [ zumy name ] [ AR tag number for Zumy] [ AR tag number for source] ')
        sys.exit()
    ar_tags = {}
    zumy_name = sys.argv[1]
    ar_tags['ar1'] = 'ar_marker_' + sys.argv[2]
    ar_tags['arZ'] = 'ar_marker_' + sys.argv[3]
    # ar_tag1 = 'ar_marker_' + sys.argv[4]
    # ar_tag2 = 'ar_marker_' + sys.argv[5]
    # ar_tag3 = 'ar_marker_' + sys.argv[6]
    # ar_tag4 = 'ar_marker_' + sys.argv[7]
    # ar_tag_arr = [ar_tag1, ar_tag2, ar_tag3, ar_tag4]

    follow_ar_tag(zumy=zumy_name, ar_tags=ar_tags)
    rospy.spin()
"""
trans: (0.03268374870994384, -0.3074980915287687, -0.020927492619987387)
rot: (0.0040673868531792825, -0.0019052957644646313, 0.7380182906831387, 0.674765758489103)

trans: (-0.00919398509223357, 0.32756589990405705, -0.011873892866908209)
rot: (-0.003395286622595306, 0.0014976342129833231, -0.0016685129096178364, 0.9999917225583345)

"""