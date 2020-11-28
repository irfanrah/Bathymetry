#!/usr/bin/env python

import rospy
import xlsxwriter
import time
from time import strftime 
from std_msgs.msg import String

def PosX(datax):
	global PosisiX
	PosisiX = datax.data
	rospy.loginfo(datax.data)
def PosY(datay):
	global PosisiY
	PosisiY = datay.data
	rospy.loginfo(datay.data)
def PosZ(dataz):
	global PosisiZ
	PosisiZ = dataz.data
	rospy.loginfo(dataz.data)


waktu = strftime("%H:%M:%S")

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook(waktu+'.xlsx')
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
worksheet.write(1, 2, 'Sumbu X')
worksheet.write(1, 3, 'Sumbu Y')
worksheet.write(1, 4, 'Sumbu Z')


# Start from the first cell. Rows and columns are zero indexed.
row = 2
col = 2


if __name__ == '__main__':
	rospy.init_node('dataexcel', anonymous=True)
	rospy.Subscriber("/makarax/PosX", String, PosX)
	rospy.Subscriber("/makarax/PosY", String, PosY)
	rospy.Subscriber("/makarax/PosZ", String, PosZ)
	rate = rospy.Rate(1)
	PosisiX = None
	PosisiY = None
	PosisiZ = None
	
	while not rospy.is_shutdown():
		worksheet.write(row,col,PosisiX)
		worksheet.write(row, col + 1, PosisiY)
		worksheet.write(row, col + 2, PosisiZ)
		row += 1
		rate.sleep()
	workbook.close()


