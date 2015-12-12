#!/usr/bin/python

import rospy

from geometry_msgs.msg import Twist
from threading import Condition
from zumy import Zumy
from std_msgs.msg import String,Header,Float32MultiArray
from sensor_msgs.msg import Imu

import socket,time

class ZumyROS:
  def __init__(self):
    self.zumy = Zumy()
    rospy.init_node('zumy_ros')
    self.cmd = (0,0)
    rospy.Subscriber('cmd_vel', Twist, self.cmd_callback)
    self.lock = Condition()
    self.rate = rospy.Rate(30.0)
    self.name = socket.gethostname()
    self.heartBeat = rospy.Publisher('/' + self.name + '/heartBeat', String, queue_size=5)
    self.imu_pub = rospy.Publisher('/' + self.name + '/imu', Imu, queue_size = 1)
    self.imu_count = 0
    self.photo_pub = rospy.Publisher('/' + self.name + '/photo', Float32MultiArray, queue_size=1)

  def cmd_callback(self, msg):
    lv = 0.6
    la = 0.4
    v = msg.linear.x
    a = msg.angular.z
    r = lv*v + la*a
    l = lv*v - la*a
    self.lock.acquire()
    self.cmd = (l,r)
    self.lock.release()

  def run(self):
    while not rospy.is_shutdown():
      self.lock.acquire()
      self.zumy.cmd(*self.cmd)
      imu_data = self.zumy.read_imu()
      photo_data = Float32MultiArray()
      photo_data.data = self.zumy.read_photo()
      self.lock.release()

      imu_msg = Imu()
      imu_msg.header = Header(self.imu_count,rospy.Time.now(),self.name)
      imu_msg.linear_acceleration.x = 9.81 * imu_data[0]
      imu_msg.linear_acceleration.y = 9.81 * imu_data[1]
      imu_msg.linear_acceleration.z = 9.81 * imu_data[2]
      imu_msg.angular_velocity.x = 3.14 / 180.0 * imu_data[3]
      imu_msg.angular_velocity.y = 3.14 / 180.0 * imu_data[4]
      imu_msg.angular_velocity.z = 3.14 / 180.0 * imu_data[5]
      self.imu_pub.publish(imu_msg)
      self.photo_pub.publish(photo_data)
      self.heartBeat.publish("I am alive")
      self.rate.sleep()
      # If shutdown, turn off motors
    self.zumy.cmd(0,0)

if __name__ == '__main__':
  zr = ZumyROS()
  zr.run()

