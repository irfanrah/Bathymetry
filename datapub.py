#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import random

PozX = 0
PozY = 0
PozZ = 0

def talker():
	
	rospy.init_node('talker', anonymous=True)
	pX = rospy.Publisher("/makarax/PosX", String, queue_size=10)
	pY = rospy.Publisher("/makarax/PosY", String, queue_size=10)
	pZ = rospy.Publisher("/makarax/PosZ", String, queue_size=10)
	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		#PozX = random.randint(0,10)
		PozX = "3"
		PozY = "10"
		PozZ = "100"
		pX.publish(PozX)
		pY.publish(PozY)
		pZ.publish(PozZ)
		rospy.loginfo(PozX)
		rospy.loginfo(PozY)
		rospy.loginfo(PozZ)
		rate.sleep()
		
if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
