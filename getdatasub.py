#!/usr/bin/env python

import rospy
import xlsxwriter
import time
from time import strftime 
from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix
from brping import Ping1D

def callback(data):
	global PosisiX
	global PosisiY
	PosisiX = data.longitude
	PosisiY = data.latitude
	rospy.loginfo(PosisiX)

waktu = strftime("%H:%M:%S")

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook(waktu+'.xlsx')
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
worksheet.write(1, 2, 'Sumbu X')
worksheet.write(1, 3, 'Sumbu Y')
worksheet.write(1, 4, 'Sumbu Z')
worksheet.write(1, 5, 'Confidence')



# Start from the first cell. Rows and columns are zero indexed.
row = 2
col = 2


if __name__ == '__main__':
	rospy.init_node('dataexcel', anonymous=True)
	rospy.Subscriber("/mavros/global_position/global", NavSatFix, callback)    
	rate = rospy.Rate(2)
	pZ = rospy.Publisher("/makarax/PosZ", String, queue_size=10)
	PosisiX = None
	PosisiY = None
	PosisiZ = None
	myPing = Ping1D("/dev/ttyACM1", 115200)
	data = myPing.get_distance()


	while not rospy.is_shutdown():
		data = myPing.get_distance()
		worksheet.write(row,col,PosisiX)
		worksheet.write(row, col + 1, PosisiY)
		if data:
			worksheet.write(row, col + 2, data["distance"])
			worksheet.write(row, col + 3, data["confidence"])
			rospy.loginfo(data["distance"])
			rospy.loginfo(data["confidence"])
			pZ.publish(str(data["distance"]))
		row += 1
		rate.sleep()
	workbook.close()


