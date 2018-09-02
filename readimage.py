import numpy as np
import cv2 as cv

#load the image in gray scale

img = cv.imread("mandril_color.tif",0)

#Now set the Image window size to Normal
cv.namedWindow("image",cv.WINDOW_NORMAL)
cv.imshow('image', img)

#waitkey is the keyboard function
#If 0 is passed, it waits indefinitely for a key stroke
k = cv.waitKey(0)

if k==27:
        cv.destroyAllWindows() #Destroy all open windows by program
elif k ==ord('s'):
    cv.imwrite("mandril_color.png", img) #Write teh image to any other location
    cv.destroyAllWindows()



