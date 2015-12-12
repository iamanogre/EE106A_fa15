#!/usr/bin/env python
import rospy
import sys

from std_msgs.msg import Float32MultiArray

def talker():
	message = Float32MultiArray()
	array = [0.1, 0.2, 0.3]
	message.data = array
	pub = rospy.Publisher('chatter', Float32MultiArray, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		pub.publish(message)
		rate.sleep()
 
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass