import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('messi-face.jpg', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(imgray, template, cv2.TM_CCOEFF_NORMED)
#print(res)
threshold = 0.5;
loc = np.where(res >= threshold)
print(loc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0,255,0), 2)

cv2.imshow('messi', img)
cv2.imshow('face-template', template)

cv2.waitKey(0)
cv2.destroyAllWindows()