#!/usr/bin/env python
import rospy
import sys

from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3
from kalman_zumy.srv import ImuSrv, ImuSrvResponse


class ImuService:
  #Callback for when an image is received
  def imuReceived(self, message):
    #Save the image in the instance variable
    self.last_acc = message.linear_acceleration
    self.last_gyro = message.angular_velocity
    self.filtered_acc.x = 0.75 * self.filtered_acc.x + 0.25 * message.linear_acceleration.x
    self.filtered_acc.y = 0.75 * self.filtered_acc.y + 0.25 * message.linear_acceleration.y
    self.filtered_acc.z = 0.75 * self.filtered_acc.z + 0.25 * message.linear_acceleration.z
    self.filtered_gyro.x = 0.75 * self.filtered_gyro.x + 0.25 * message.angular_velocity.x
    self.filtered_gyro.y = 0.75 * self.filtered_gyro.y + 0.25 * message.angular_velocity.y
    self.filtered_gyro.z = 0.75 * self.filtered_gyro.z + 0.25 * message.angular_velocity.z
    self.new = True

    #Print an alert to the console
    #print(rospy.get_name() + ":Imu received!")

  #When another node calls the service, return the last image
  def getLastImu(self, request):
    if self.new:
      self.new = False # Record the fact that no new measurements are available
      #Return the last measurement

      print(self.filtered_acc)

      return ImuSrvResponse(self.last_acc,self.last_gyro,\
                            self.filtered_acc,self.filtered_gyro)
    else:
      return None

  def __init__(self,mname):
#    mname = "zumy7b"
    print "Launching IMU sevice for " + mname

    #Create variables to store the last IMU data received
    self.last_acc = Vector3()
    self.last_gyro = Vector3()
    self.filtered_acc = Vector3()
    self.filtered_gyro = Vector3()
    self.new = False

    #Initialize the node
    rospy.init_node(mname +'_imu_listener')

    #Subscribe to the imu topic
    self.topic = "/" + mname + "/imu"
    rospy.Subscriber(self.topic, Imu, self.imuReceived)

    #Create the service
    rospy.Service('last_imu', ImuSrv, self.getLastImu)
    print "Created service 'last_imu' on node /" + mname + "_imu_listener"

  def run(self):
    rospy.spin()

#Python's syntax for a main() method
if __name__ == '__main__':
  # try:
  #     mname = rospy.get_param('~mname')
  # except KeyError:
  #     print "value not set--no clue why this won't work\nresorting to 'zumy7b'"
  #     mname = 'zumy7b'
  mname = sys.argv[1]
  node = ImuService(mname)
  node.run()

