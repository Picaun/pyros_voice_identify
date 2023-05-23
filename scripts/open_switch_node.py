#!/usr/bin/env python3
#coding:utf-8

import rospy
from std_msgs.msg import String
RESET_FLAG = False


def callback(data):
     global RESET_FLAG
     RESET_FLAG = True

def open_switch():
     global RESET_FLAG
     pub = rospy.Publisher('open_switch', String, queue_size=1)
     rospy.init_node('open_switch_node', anonymous=True)

     
     rate = rospy.Rate(10) # 10hz
     while not rospy.is_shutdown():
         rospy.Subscriber("reset_switch",String,callback)
         if RESET_FLAG:
             RESET_FLAG = False
             rospy.signal_shutdown("reset!!")
             
         send_str = "1"
         rospy.loginfo(send_str)
         pub.publish(send_str)
         rate.sleep()

if __name__ == '__main__':
	try:
		open_switch()
	except rospy.ROSInterruptException:
		pass

