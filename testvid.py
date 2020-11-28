import cv2
import numpy as np

cap = cv2.VideoCapture('vid1.mp4',0)
cap1 = cv2.VideoCapture('vid2.mp4',0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):

	ret, frame = cap.read()
	ret1, frame1 = cap1.read()
	if ret == True: 

		both = np.concatenate((frame, frame1), axis=1)
		both.shape == (frame.shape[0], 2*frame.shape[1])

		out.write(both)
		cv2.imshow('frame', both)

		
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	else: 
		break



cap.release()
out.release()
cv2.destroyAllWindows()
