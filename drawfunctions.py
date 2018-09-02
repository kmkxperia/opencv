import numpy as np
import cv2 as cv

#create a black image
img = np.zeros((512,512,3), np.uint8)


# Draw a diagonal blue line with thickness of 5 px BGR
img = cv.line(img,(0,0),(511,511),(0,0,255),5)


#Rectangle
img = cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

#Circle
img = cv.circle(img,(447,63), 63, (0,0,255), -1)

#Write Text on the image
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)
cv.imshow("balkboard", img)
#cv.waitKey(0)
#cv.destroyAllWindows()
