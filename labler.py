import sys
from hardetect import faceCoordinates

output = open(sys.argv[1],'w')
cascade = sys.argv[2]
images = sys.argv[3:]

for image in images:
	x = faceCoordinates(image, cascade)
	output.write( image + " : " + str(x)[2:-2] + "\n")
