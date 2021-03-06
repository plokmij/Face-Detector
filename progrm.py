import cv2
import numpy as np
from matplotlib import pyplot as plt

def preprocess(img)
	image = cv2.imread(img)
	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray_image,(15,15),0)
	th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

	edges = cv2.Canny( th3, 100, 200)
	backdel = edges - gray_image
	fileName = img + "prepro"
	cv2.imwrite('fileName', backdel )


preprocess('aa.jpeg')
