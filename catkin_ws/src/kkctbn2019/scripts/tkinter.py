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
from sensor_msgs.msg import NavSatFix



ori = np.zeros([480,640,3], dtype=np.uint8)
PosisiX = 0
PosisiY = 0
PosisiZ = 0
count = 0
path = 'maps2.png'

def image_callback(img):
	global ori
	bridge = CvBridge()
	ori = bridge.imgmsg_to_cv2(img)
	
def callback(data):
	global PosisiX
	global PosisiY
	PosisiX = data.longitude
	PosisiY = data.latitude
	rospy.loginfo(PosisiX)
	
	
def PosZ(dataz):
	global PosisiZ
	PosisiZ = dataz.data
	rospy.loginfo(dataz.data)


	
if __name__ == '__main__':
	rospy.init_node('gcs', anonymous=True)
	image_subscriber = rospy.Subscriber("/makarax/image", ROSImage, image_callback)
	rospy.Subscriber("/mavros/global_position/global", NavSatFix, callback)
	rospy.Subscriber("/makarax/PosZ", String, PosZ)
	master = Tkinter.Tk()
	master.title("Config")
	master.geometry("1200x1000")
	ori_label = Tkinter.Label(master=master, image=None)
	ori_label.place(x = 3 , y = 3)
	imga = ImageTk.PhotoImage(Image.open(path))
	Tkinter.Label(master=master, image = imga).place(x = 650 , y = 3)
	Tkinter.Label(master=master, text="X", fg='green',bg = 'white',bd = '10' ,font=("Helvetica", 25)).place(x = 100, y = 495)
	Tkinter.Label(master=master, text="Y", fg='blue',bg = 'white',bd = '10' , font=("Helvetica", 25)).place(x = 100, y = 580)
	Tkinter.Label(master=master, text="Z", fg='red',bg = 'white',bd = '10' , font=("Helvetica", 25)).place(x = 450, y = 495)
	Tkinter.Label(master=master, text="Confidence", fg='black',bg = 'white',bd = '10' , font=("Helvetica", 25)).place(x = 400, y = 580)
	#Tkinter.Label(master=master, text="X", fg='black',bg = 'white',bd = '0' ,font=("Helvetica", 25)).place(x = 950, y = 500) #kapal
	
	while not rospy.is_shutdown():
		if ori is not None:
			b,g,r = cv2.split(ori)
			img = cv2.merge((r,g,b)) 
			im = Image.fromarray(img)
			imgtk = ImageTk.PhotoImage(image=im)
			ori_label.config(image=imgtk)
			count = count + 1
			if count >= 100:
				#Tkinter.Label(master=master, text=PosisiX, fg='black',bg = 'green',bd = '3' ,font=("Helvetica", 25)).place(x = 50, y = 540)
				Tkinter.Label(master=master, text=106.8261649, fg='black',bg = 'green',bd = '3' ,font=("Helvetica", 25)).place(x = 50, y = 540)
				#Tkinter.Label(master=master, text=PosisiY, fg='black',bg = 'blue',bd = '3' , font=("Helvetica", 25)).place(x = 50, y = 630)
				Tkinter.Label(master=master, text=-6.3625941, fg='black',bg = 'blue',bd = '3' , font=("Helvetica", 25)).place(x = 50, y = 630)
				#Tkinter.Label(master=master, text=PosisiZ, fg='black',bg = 'red',bd = '3' , font=("Helvetica", 25)).place(x = 420, y = 580)
				Tkinter.Label(master=master, text=100, fg='black',bg = 'red',bd = '3' , font=("Helvetica", 25)).place(x = 420, y = 540)
				Tkinter.Label(master=master, text=100, fg='black',bg = 'white',bd = '3' , font=("Helvetica", 25)).place(x = 420, y = 630)
				count = 0
		master.update()
