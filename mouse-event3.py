import numpy as np
import cv2

def click_event(event, x, y):
    if event == cv2.EVENT_LBUTTONDOWN:
        b = img[x,y,0]
        g = img[x,y,1]
        r = img[x,y,2]

    cv2.circle(img,(x,y),3,(0,255,0),-1)
    myimg = np.zeros((512,512,3),np.uint8)

    myimg[:] = [b,g,r]
    cv2.imshow('color',myimg)

img = cv2.imread('lena.jpg',1)
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
