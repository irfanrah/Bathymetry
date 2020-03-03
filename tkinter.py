#!/usr/bin/env python

import cv2
import rospy
import Tkinter
from PIL import Image, ImageTk
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image as ROSImage
import numpy as np
import random
from std_msgs.msg import String




ori = np.zeros([480,640,3], dtype=np.uint8)
PosisiX = 0
PosisiY = 0
PosisiZ = 0

path = 'maps.jpg'

def image_callback(img):
	global ori
	bridge = CvBridge()
	ori = bridge.imgmsg_to_cv2(img)
	
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


	
if __name__ == '__main__':
	rospy.init_node('gcs', anonymous=True)
	image_subscriber = rospy.Subscriber("/makarax/image", ROSImage, image_callback)
	rospy.Subscriber("/makarax/PosX", String, PosX)
	rospy.Subscriber("/makarax/PosY", String, PosY)
	rospy.Subscriber("/makarax/PosZ", String, PosZ)
	master = Tkinter.Tk()
	master.title("Config")
	master.geometry("1200x1000")
	ori_label = Tkinter.Label(master=master, image=None)
	ori_label.place(x = 3 , y = 3)
	imga = ImageTk.PhotoImage(Image.open(path))
	Tkinter.Label(master=master, image = imga).place(x = 650 , y = 3)
	Tkinter.Label(master=master, text="X", fg='green',bg = 'white',bd = '10' ,font=("Helvetica", 25)).place(x = 50, y = 495)
	Tkinter.Label(master=master, text="Y", fg='blue',bg = 'white',bd = '10' , font=("Helvetica", 25)).place(x = 180, y = 495)
	Tkinter.Label(master=master, text="Z", fg='red',bg = 'white',bd = '10' , font=("Helvetica", 25)).place(x = 310, y = 495)
	Tkinter.Label(master=master, text="X", fg='black',bg = 'white',bd = '0' ,font=("Helvetica", 25)).place(x = 950, y = 500) #kapal
	Tkinter.Label(master=master, text=PosisiX, fg='black',bg = 'green',bd = '3' ,font=("Helvetica", 25)).place(x = 40, y = 540)
	Tkinter.Label(master=master, text=PosisiY, fg='black',bg = 'blue',bd = '3' , font=("Helvetica", 25)).place(x = 170, y = 540)
	Tkinter.Label(master=master, text=PosisiZ, fg='black',bg = 'red',bd = '3' , font=("Helvetica", 25)).place(x = 300, y = 540)
	
	while not rospy.is_shutdown():
		if ori is not None:
			b,g,r = cv2.split(ori)
			img = cv2.merge((r,g,b)) 
			im = Image.fromarray(img)
			imgtk = ImageTk.PhotoImage(image=im)
			ori_label.config(image=imgtk)
		master.update()
