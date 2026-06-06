import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",help="path to file")
args=vars(ap.parse_args())

#get the image
image = cv2.imread(args["image"])

#convert to hsv for more comprehensive color
hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

#colors
boundaries = [
    ([100, 50, 50], [140, 255, 255]), # Comprehensive Blues
    ([35, 50, 50], [85, 255, 255]),   # Comprehensive Greens
    ([15, 50, 50], [35, 255, 255]),   # Comprehensive Yellows/Golds
    
    # Red is tricky because it wraps around the 0 mark in HSV. 
    # This range catches the primary red spectrum:
    ([0, 50, 50], [10, 255, 255])     
] 

for (lower,upper) in boundaries:
    #convert bounds to np arrays
    lower = np.array(lower,dtype="uint8")
    upper = np.array(upper,dtype="uint8")

    #mask
    mask = cv2.inRange(hsv_image,lower,upper)
    #convert the image
    output = cv2.bitwise_and(image,image, mask=mask)

    cv2.imshow("images",np.hstack([image,output]))
    cv2.waitKey(0)