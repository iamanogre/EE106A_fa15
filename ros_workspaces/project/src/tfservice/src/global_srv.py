#!/usr/bin/env python
import tf
import rospy
import sys
import math
import numpy as np
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import Transform, Vector3, Twist, Quaternion
import exp_quat_func as eqf
import kin_func_skeleton as kfs

from tfservice.srv import *

class GlobalService:

    def getPosition(self, request):

        # request to getPosition contains zumy tag
        zumy = request.zumy
        # print(zumy)
        zumyAR = self.zumy_dict[request.zumy] 
        try:
            #print("above")
            (self.trans, self.rot) = self.listener.lookupTransform(self.origin, zumyAR, rospy.Time(0))
            #print("below")
            #(trans, rot) = listener.lookupTransform(ar_tags['arZ'], ar_tags['ar1'], rospy.Time(0))
            #(trans, rot) = listener.lookupTransform('ar_marker_5', 'ar_marker_3', rospy.Time(0))
            quaternion = np.array([self.rot[0], self.rot[1], self.rot[2], self.rot[3]])
            omega, theta = eqf.quaternion_to_exp(quaternion)
            translation = np.array([self.trans[0], self.trans[1], self.trans[2]])
            g_SZ = eqf.create_rbt(omega, theta, translation)
            self.zumy_updated[zumy] = True
            position = g_SZ[0:3, 3]
            #print("position: " + str(position))

            rotation = g_SZ[0:3, 0:3]
            omega, theta = eqf.find_omega_theta(rotation)  
            if(omega[2] < 0):
                theta = 2*np.pi - theta
            #print(omega)
            #print(theta*180/np.pi)

            # assign values -> should now to be dictionaries
            self.zumy_pos[zumy] = position
            self.zumy_theta[zumy] = theta

            # send over position and theta over service depending on which zumy
            # print(self.zumy_updated[zumy])
            # print(self.zumy_theta[zumy])
            # print(self.zumy_pos[zumy])

        except:
            self.zumy_updated[zumy] = False
            print("failed")
        return globalSrvResponse(self.zumy_updated[zumy], self.zumy_theta[zumy], self.zumy_pos[zumy])

    def __init__(self, zumy_dict, originARtag, zumy_pos, zumy_theta, zumy_updated):
        print "Launching Global Camera service"

        # zumy and origin AR tags
        self.origin = originARtag
        self.zumy_dict = zumy_dict

        self.zumy_pos = zumy_pos
        self.zumy_theta = zumy_theta
        self.zumy_updated = zumy_updated 

        #Initialize the node
        rospy.init_node('global_camera')

        # tf listener
        self.trans = [0, 0, 0]
        self.rot = [0, 0, 0, 0]
        self.listener = tf.TransformListener()
        self.rate = rospy.Rate(10)

        # create the service
        rospy.Service('global_pos', globalSrv, self.getPosition)
        print "Created service 'global_pos' on node global_camera"

    def run(self):
        rospy.spin()

if __name__=='__main__':
    if len(sys.argv) < 6:
        print('Use: follow_ar_tag_manual.py zumy1 [AR tag number for Zumy1] zumy2 [AR tag for Zumy2] [ AR tag number for origin] ')
        sys.exit()
    
    # dictionary to convert from zumy name to zumy ar marker
    zumy1 = sys.argv[1]
    zumy1ARtag = 'ar_marker_' + sys.argv[2]
    zumy2 = sys.argv[3]
    zumy2ARtag = 'ar_marker_' + sys.argv[4]
    originARtag = 'ar_marker_' + sys.argv[5]
    zumy_dict = {zumy1: zumy1ARtag, zumy2:zumy2ARtag}

    # arguments to pass to global service
    position = [0, 0, 0]
    theta = 0
    updated = False

    # zumy position dict, zumy theta reading, zumy updated reading
    zumy_pos = {zumy1: position, zumy2: position}
    zumy_theta = {zumy1: theta, zumy2: theta}   
    zumy_updated = {zumy1: updated, zumy2: updated}   
    
    node = GlobalService(zumy_dict, originARtag, zumy_pos, zumy_theta, zumy_updated)
    node.run()