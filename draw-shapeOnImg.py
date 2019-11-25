import cv2
import numpy as np
#img = cv2.imread('lena.jpg', 1)
#CREATE IMAGE WITH NUMPY ZEROS
img = np.zeros([512,512,3], np.uint8)
print(type(img))
img = cv2.line(img, (0,0), (255,255), (0,255,0), 5)
img = cv2.arrowedLine(img,(0,255),(255,255),(0,0,255),5)
img = cv2.rectangle(img,(384,10),(500,128),(0,0,255),5)
img = cv2.rectangle(img,(384,130),(500,228),(0,0,255),-1)
img = cv2.circle(img, (447,63),63, (0,255,0),-1)
font = cv2.FONT_HERSHEY_DUPLEX
img = cv2.putText(img, 'OpenCV',(50,300), font, 4, (255,255,255),3, cv2.LINE_AA)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()