"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('aa.jpeg', 0 )
gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img,(5,5),0)
th3 = cv2.adaptiveThreshold(gimg,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

plt.subplot(121),plt.imshow(gimg),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(gth3),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

"""
import cv2
from matplotlib import pyplot as plt

image = cv2.imread('aa.jpeg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray_image,(5,5),0)
th3 = cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)


cv2.imshow('gray_image',gray_image) 
cv2.waitKey(0)                 # Waits forever for user to press any key
cv2.destroyAllWindows() 
