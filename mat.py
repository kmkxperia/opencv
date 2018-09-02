import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt

img= cv.imread("mandril_gray.tif", 0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
