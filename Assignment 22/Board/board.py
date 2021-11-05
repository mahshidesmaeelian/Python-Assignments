import cv2
import numpy as np

img1 = cv2.imread("Board/board - origin.bmp" , 0)
img2 = cv2.imread("Board/board - test.bmp" , 0)


result = cv2.subtract(img1,img2)


cv2.imwrite('Board/board.jpg' , result)

cv2.imshow('output' , result)

cv2.waitKey()