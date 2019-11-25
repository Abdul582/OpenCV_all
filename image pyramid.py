import numpy as np
import cv2

#GAUSSIOAN Pyramid

img = cv2.imread('lena.jpg')
lowerR = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lowerR)

HigherR = cv2.pyrUp(lowerR)

cv2.imshow('original',img)
cv2.imshow('Lower Resolution', lowerR)
cv2.imshow('Lower R 2', lr2)
cv2.imshow('Higher Resolution 1', HigherR)

cv2.waitKey(0)
cv2.destroyAllWindows()