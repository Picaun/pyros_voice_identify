#!/usr/bin/env python3
#coding:utf-8

import rospy
from std_msgs.msg import String

def reset_switch():
     pub = rospy.Publisher('reset_switch', String, queue_size=4)
     rospy.init_node('reset_switch_node', anonymous=True)
     rate = rospy.Rate(50) # 50hz
     for i in range(1,20):
         send_str = "-1"
         rospy.loginfo(send_str)
         pub.publish(send_str)
         rate.sleep()

if __name__ == '__main__':
	try:
		reset_switch()
	except rospy.ROSInterruptException:
		pass
