import cv2 as cv
import numpy as np

img = cv.imread("resources/black.png")
#cv.imshow('img',img)
#cv.waitKey(0)
px = img[200,200]
print(px)

px = img[200,200,0]
print(px)
print (img.shape)
print (img.size)

#Edit Single pixel value

img[210,340] = [255,255,255]

#Draw a line by modofying the pixel values BGR
for x in range(0, 200):
    img[x,x] = [255,0,255]

#Copy image from one location to Other ROI Region of ntrest
imCrop = img[200:220, 210:220]
#cv.imshow("Image", imCrop)
#cv.waitKey(0)
img[200:220, 380:390] = imCrop

cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()

#img.itemset((10,10,2),100)
#img.item(10,10,2)
#cv.imshow('img',img)
#cv.waitKey(0)
