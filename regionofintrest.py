
#Import the Required Packages
import cv2 as cv
import numpy as np



# Read image
im = cv.imread("resources/black.png")

# ----Select ROI-----
#const cv::String & 	windowName,
#Mat 	img,
#bool 	showCrossair = true,
#bool 	fromCenter = true
#--------------------
r = cv.selectROI("Image", im, False, False)

print (r)
print (r[0])
print (r[1])
print (r[2])
print (r[3])


#Crop image
#crop_img = img[y:y+h, x:x+w]
imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]


# Note this code does not work. 
# Specify a vector of rectangles (ROI) 
rects = []
fromCenter = false
# Select multiple rectangles
selectROI("Image", im, rects, fromCenter)
# Display cropped image
cv.imshow("Image", imCrop)
cv.waitKey(0)
