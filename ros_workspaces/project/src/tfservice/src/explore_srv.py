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
import random

from tfservice.srv import *

class ExploreService:

    def sendPosition1(self, request):
        
        hard_stop = False

        # moving average 
        self.photo_readings[1:] = self.photo_readings[0:-1]
        self.photo_readings[0] = request.photo_data
        photo_avg = np.apply_along_axis(np.mean,0,self.photo_readings)
        print(photo_avg)

        zumyX = request.position[0]
        zumyY = request.position[1]
        self.zumy1_x = zumyX
        self.zumy1_y = zumyY
        #print(str(photo_avg) + " " + str(self.keepExploring))

        # read the request fields and send position to zumy
        if (self.keepExploring == False):
            # just tell all zumies where it should go
            return exploreSrvResponse([self.x_desFinal, self.y_desFinal], self.zumy1_hard_stop)
        else: 
            #string zumy_name
            #float32[] position
            #float32[] photo_data

            # interpret zumy position and photo data and give it new position to go to
            """
            topLeft = request.photo_data[0]
            botLeft = request.photo_data[1]
            topRight = request.photo_data[2]
            botRight = request.photo_data[3]
            """
            
            #maxValue = max(request.photo_data)

            frontMax = float(max(photo_avg[0],photo_avg[2]))
            backMax = float(max(photo_avg[1], photo_avg[3]))
            #return exploreSrvResponse([0.2, 0.3])
            #print(str(type(frontMax)) + " thres: " + str(type(self.front_thres)))
            frontNoLight = frontMax < self.front_thres
            backNoLight =  backMax < self.back_thres
            #print(str(frontNoLight) + " back: " + str(backNoLight))
            if (not frontNoLight or not backNoLight):
            # case where we hit over a threshold -> assign self.x and self.y as new position
                self.keepExploring = False
                self.x_desFinal = zumyX
                self.y_desFinal = zumyY
                self.zumy1_hard_stop = True
                return exploreSrvResponse([self.x_desFinal, self.y_desFinal], self.zumy1_hard_stop)

            if(request.finished):

                #print(str(frontNoLight and backNoLight))
                # case keep exploring --> and account for random fluctuations
                if (frontNoLight and backNoLight):
                    self.x_des1 = zumy1_region[0] + random.random()*(zumy1_region[1] - zumy1_region[0])
                    self.y_des1 = zumy1_region[2] + random.random()*(zumy1_region[3] - zumy1_region[2])

                    while(self.x_des1 <= zumy1_region[0] or self.x_des1 >= zumy1_region[1]):
                        self.x_des1 = zumy1_region[0] + random.random()*(zumy1_region[1] - zumy1_region[0])
                    while(self.y_des1 <= zumy1_region[2] or self.y_des1 >= zumy1_region[3]):
                        self.y_des1 = zumy1_region[2] + random.random()*(zumy1_region[3] - zumy1_region[2])

                    print(str(self.x_des1) + " " + str(self.y_des1))

                    if (self.x_des1 <= 0.2 and self.x_des1 > 0):
                        self.x_des1 = l1*2 - self.x_des1
                    elif (self.x_des1 < 0):
                        self.x_des1 = l1*2 + self.x_des1
                    if (self.y_des1 <= 0.2 and self.y_des1 > 0):
                        self.y_des1 = l2*2 - self.y_des1
                    elif (self.y_des1 < 0):
                        self.y_des1 = l2*2 + self.y_des1
                    
                    return exploreSrvResponse([self.x_des1, self.y_des1], self.zumy1_hard_stop)
                # else:
                # # case where we hit over a threshold -> assign self.x and self.y as new position
                #     self.keepExploring = False
                #     #self.x = zumyX
                #     #self.y = zumyY
                #     return exploreSrvResponse([self.x_des1, self.y_des1])
            else:
                return exploreSrvResponse([self.x_des1, self.y_des1], self.zumy1_hard_stop)

    def sendPosition2(self, request):

        hard_stop = False
        
        self.photo_readings[1:] = self.photo_readings[0:-1]
        self.photo_readings[0] = request.photo_data
        photo_avg = np.apply_along_axis(np.mean,0,self.photo_readings)
        #self.keepExploring = True #REMOVE AFTERWARDS OR DOESNT STOP
        print(str(photo_avg) + " " + str(self.keepExploring))

        zumyX = request.position[0]
        zumyY = request.position[1]
        self.zumy2_x = zumyX
        self.zumy2_y = zumyY

        # read the request fields and send position to zumy
        if (self.keepExploring == False):
            # just tell all zumies where it should go
            hard_stop = self.findHardStop()
            return exploreSrvResponse([self.x_desFinal, self.y_desFinal], hard_stop)
        else: 
            #string zumy_name
            #float32[] position
            #float32[] photo_data

            # interpret zumy position and photo data and give it new position to go to
            """
            topLeft = request.photo_data[0]
            botLeft = request.photo_data[1]
            topRight = request.photo_data[2]
            botRight = request.photo_data[3]
            """
            

            #maxValue = max(request.photo_data)

            frontMax = float(max(photo_avg[0],photo_avg[2]))
            backMax = float(max(photo_avg[1], photo_avg[3]))
            #return exploreSrvResponse([0.2, 0.3])
            #print(str(type(frontMax)) + " thres: " + str(type(self.front_thres)))
            frontNoLight = frontMax < 10#self.front_thres
            backNoLight =  backMax < 10#self.back_thres
            #print(str(frontNoLight) + " back: " + str(backNoLight))

            # NEVER GOING TO EXECUTE
            if (not frontNoLight or not backNoLight):
            # case where we hit over a threshold -> assign self.x and self.y as new position
                self.keepExploring = False
                self.x_desFinal = zumyX
                self.y_desFinal = zumyY
                hard_stop = self.findHardStop()
                return exploreSrvResponse([self.x_desFinal, self.y_desFinal], hard_stop)


            if(request.finished):

                #print(str(frontNoLight and backNoLight))
                # case keep exploring --> and account for random fluctuations
                if (frontNoLight and backNoLight):
                    self.x_des2 = zumy2_region[0] + random.random()*(zumy2_region[1] - zumy2_region[0])
                    self.y_des2 = zumy2_region[2] + random.random()*(zumy2_region[3] - zumy2_region[2])

                    while(self.x_des2 <= zumy2_region[0] or self.x_des2 >= zumy2_region[1]):
                        self.x_des2 = zumy2_region[0] + random.random()*(zumy2_region[1] - zumy2_region[0])
                    while(self.y_des2 <= zumy2_region[2] or self.y_des2 >= zumy2_region[3]):
                        self.y_des2 = zumy2_region[2] + random.random()*(zumy2_region[3] - zumy2_region[2])
                    
                    print(str(self.x_des2) + " " + str(self.y_des2))

                    if (self.x_des2 <= 0.2 and self.x_des2 > 0):
                        self.x_des2 = zumy2_region[1] - self.x_des2
                    elif (self.x_des2 < 0):
                        self.x_des2 = zumy2_region[1] + self.x_des2
                    if (self.y_des2 <= 0.2 and self.y_des2 > 0):
                        self.y_des2 = zumy2_region[3] - self.y_des2
                    elif (self.y_des2 < 0):
                        self.y_des1 = zumy2_region[3]+ self.y_des2
                    hard_stop = self.findHardStop()


                    return exploreSrvResponse([self.x_des2, self.y_des2], hard_stop)
                # else:
                # # case where we hit over a threshold -> assign self.x and self.y as new position
                #     self.keepExploring = False
                #     #self.x = zumyX
                #     #self.y = zumyY
                #     return exploreSrvResponse([self.x_des1, self.y_des1])
            else:
                hard_stop = self.findHardStop()
                return exploreSrvResponse([self.x_des2, self.y_des2], hard_stop)

    # returns whether or not to stop depending on 
    def findHardStop(self):
        deltax = abs(self.zumy1_x - self.zumy2_x)
        deltay = abs(self.zumy1_y - self.zumy2_y)
        distance = pow(pow(deltax, 2) + pow(deltay, 2), 0.5)
        return not (distance >= 0.2)

    def __init__(self, front, back, l1, l2):
        print "Launching Explore service"

        # keep exploring flag
        self.keepExploring = True
        self.front_thres = front
        self.back_thres = back

        #Initialize the node
        rospy.init_node('explore_node')

        # arguments to pass to explore service
        #self.x = 0
        #self.y = 0
        self.x_desFinal = 0.5
        self.y_desFinal = 0.5

        self.zumy1_x = 0
        self.zumy1_y = 0
        self.zumy1_hard_stop = False

        self.zumy2_x = 0
        self.zumy2_y = 0 

        self.x_des1 = l1
        self.y_des1 = l2

        self.x_des2 = 1.0
        self.y_des2 = 0.5


        zeros = [0.0,0.0,0.0,0.0]
        self.photo_readings = [zeros,zeros,zeros,zeros,zeros]

        # create the service
        rospy.Service('explore1', exploreSrv, self.sendPosition1)
        rospy.Service('explore2', exploreSrv, self.sendPosition2)
        print "Created service 'explore1 and explore2' on node explore_node"

    def run(self):
        rospy.spin()

if __name__=='__main__':
    if len(sys.argv) != 5:
        print('Usage: explore_srv.py front_thres back_thres length1 length2') 
    front = float(sys.argv[1])
    back = float(sys.argv[2])
    
    # distance regions stuff
    l1 = float(sys.argv[3])
    l2 = float(sys.argv[4])
    #       1 = lowerbound, 2 = upperbound
    # exploring regions [x1, x2, y1, y2]
    bound = 0.05
    zumy1_region = [0+bound,  l1*2-bound,  (l2*2)/3+bound,  l2*2-bound]
    zumy2_region = [0+bound,  l1*2-bound,  0+bound,  (l2*2)/3-bound]

    # array of photo data readings
    x_steps = math.ceil(l1*2/(0.3))
    y_steps = math.ceil(l2*2/(0.3))

    array = np.zeros((y_steps, x_steps))
    print(array)

    # run the node
    node = ExploreService(front, back, l1, l2)
    node.run()