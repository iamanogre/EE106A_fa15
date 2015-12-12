#!/usr/bin/env python
import rospy
import sys

import math
import numpy as np
import exp_quat_func as eqf

from geometry_msgs.msg import Quaternion
from tf2_msgs.msg import TFMessage
from tfservice.srv import *

class TfService:
  def tfReceived(self, message):
    #print(message)
    ar_tag = int(message.transforms[0].child_frame_id[-1])
    zumy_cam = message.transforms[0].header.frame_id
    # print(ar_tag)
    # print(zumy_cam)
    # print(ar_tag in self.ar_tag_arr)
    # print(zumy_cam in self.zumy_from_cam.keys())
    # print(self.ar_tag_arr)
    # print(self.zumy_from_cam.keys())
    if (ar_tag in self.ar_tag_arr and zumy_cam in self.zumy_from_cam.keys()):
      self.tf = message
      zumy = self.zumy_from_cam[zumy_cam]
      #print(zumy)
      self.zumy_updated[zumy] = True
      self.findPosition(zumy, ar_tag)

  def findPosition(self, zumy, ar_tag):

    #Finds information relative to the AR which it is looking at
    transform = self.tf.transforms[0].transform
    translation = transform.translation
    rotation = transform.rotation
    quaternion = np.array([rotation.x, rotation.y,rotation.z, rotation.w])
    omega, theta = eqf.quaternion_to_exp(quaternion)
    translation = np.array([translation.x, translation.y, translation.z])
    g = eqf.create_rbt(omega, theta, translation)
    g_inv = eqf.inverse_g(g)

    #This is just to make it easy to understand the ables 
    if(omega[1] < 0):
      theta =  2*np.pi - theta

    #Calculates the position of the zumy and orientation relative to the Origin
    if (ar_tag == self.ar_tag_arr[0]): # picked up tag at (1,0)
      g_0A = np.array([[1, 0, 0, l1], [0, 0, 1, 0], [0, -1, 0, 0], [0, 0, 0, 1]])
      self.zumy_theta[zumy] = 2*np.pi - theta   
    elif (ar_tag == self.ar_tag_arr[1]): # picked up tag at (0,1)
      g_0A = np.array([[0, 0, 1, 0], [-1, 0, 0, l2], [0, -1, 0, 0], [0, 0, 0, 1]])

      if(np.pi/2 - theta > 0):
        self.zumy_theta[zumy] = np.pi/2 - theta
      else:
        self.zumy_theta[zumy] = np.pi - theta + 0.75*2*np.pi

    elif (ar_tag == self.ar_tag_arr[2]): # picked up tag at (2,1)
      g_0A = np.array([[0, 0, -1, l1*2], [1, 0, 0, l2], [0, -1, 0, 0], [0, 0, 0, 1]])

      if(0.75*2*np.pi - theta < 0):
        self.zumy_theta[zumy] = 0.75*2*np.pi + abs(0.75*2*np.pi - theta)
      else:
        self.zumy_theta[zumy] = 0.75*2*np.pi - theta
      #print(self.theta)
    elif (ar_tag == self.ar_tag_arr[3]): # picked up tag at (1,2)
      g_0A = np.array([[-1, 0, 0, l1], [0, 0, -1, l2*2], [0, -1, 0, 0], [0, 0, 0, 1]])

      if(np.pi - theta < 0):
        self.zumy_theta[zumy] = 3*np.pi - theta
      else:
        self.zumy_theta[zumy] = np.pi - theta

    position = np.dot(g_0A, g_inv)

    #Easy fix to make angle out of +ve axis (out of floor)
    self.zumy_theta[zumy] = 2*np.pi - self.zumy_theta[zumy] 

    # modifty position, theta (w/ respect to ar_tag)
    self.zumy_pos[zumy] = position[0:3, 3]
    #print(omega)
    #print("theta: " + str(self.theta*180/np.pi))

  # When another node calls the service, return the last image
  def getLastTf(self, request):
    zumy = request.zumy
    #print(zumy)
    value = self.zumy_updated[zumy] # grab current value of zumy's updated
    self.zumy_updated[zumy] = False # whether self.new is true or false, turn to false!
    #print(self.zumy_theta[zumy])
    #print(self.zumy_pos[zumy])
    #print(self.zumy_theta)
    return tfSrvResponse(value, self.zumy_theta[zumy], self.zumy_pos[zumy])

  def __init__(self, zumy1, zumy2, ar_tag_arr, zumy_pos, zumy_theta, zumy_updated):
    print "Launching TF service for zumy cameras"

    self.tf = TFMessage()
    #Create variables to store the last IMU data received
    self.ar_tag_arr = ar_tag_arr

    self.zumy1cam = 'usb_cam_' + zumy1
    self.zumy2cam = 'usb_cam_' + zumy2
    # zumy dictionary -> define who is the correct zumy
    self.zumy_from_cam = {self.zumy1cam: zumy1, self.zumy2cam: zumy2}
    
    # zumy parameters
    self.zumy_pos = zumy_pos
    self.zumy_theta = zumy_theta
    self.zumy_updated = zumy_updated 

    #Initialize the node
    rospy.init_node('zumy_tf_listener')

    #Subscribe to the tf topic
    self.topic = "/tf"
    rospy.Subscriber(self.topic, TFMessage, self.tfReceived)

    #Create the service
    rospy.Service('last_tf', tfSrv, self.getLastTf)
    print "Created service 'last_tf' on node /" + "zumy_tf_listener"

  def run(self):
    rospy.spin()

#Python's syntax for a main() method
if __name__ == '__main__':
  if len(sys.argv) != 5:
    print('Usage: tf_srv.py zumy1 zumy2 length1 length2') 
    sys.exit()

  # AR tags
  ar_tag1 = 5
  ar_tag2 = 6
  ar_tag3 = 7
  ar_tag4 = 8
  ar_tag_arr = [ar_tag1, ar_tag2, ar_tag3, ar_tag4]

  zumy1 = sys.argv[1]
  zumy2 = sys.argv[2]
  l1 = float(sys.argv[3])
  l2 = float(sys.argv[4])

  # arguments to pass to global service
  position = [0, 0, 0]
  theta = 0
  updated = False

  # zumy position dict, zumy theta reading, zumy updated reading
  zumy_pos = {zumy1: position, zumy2: position}
  zumy_theta = {zumy1: theta, zumy2: theta}   
  zumy_updated = {zumy1: updated, zumy2: updated}   
  
  node = TfService(zumy1, zumy2, ar_tag_arr, zumy_pos, zumy_theta, zumy_updated)
  node.run()

