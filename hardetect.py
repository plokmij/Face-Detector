import numpy as np
import cv2


"""
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('aa.jpg',0)
#gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img, 1.3, 5)

for (x,y,w,h) in faces:
	print(x, y,)
	print(x+w, y+h)

"""

def faceCoordinates( image, cascade):
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	img = cv2.imread( image, 0)
	faces = face_cascade.detectMultiScale(img, 1.3, 5)
	return faces

print(faceCoordinates( 'aa.jpg', 'haarcascade_frontalface_default.xml'))
