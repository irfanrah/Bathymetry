#!/usr/bin/env python

import rospy
from sensor_msgs.msg import NavSatFix

 
def callback(data):
	rospy.loginfo(data.longitude)
def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("/mavros/global_position/global", NavSatFix, callback)
	rospy.spin()
	
if __name__ == '__main__':
	listener()
