import numpy as np
import cv2

# #img = cv2.imread('lena.jpg', 1)
# img = np.zeros([640,480])
#
# cv2.line(img, (0,255), (255,255), (0,0,255), 2, cv2.LINE_AA)
# cv2.circle(img,(255,300),100,(0,255,0),-1)
# cv2.putText(img,'hello cv',(0,460),cv2.FONT_ITALIC,4,(255,0,0),5)
#
# cv2.imshow('image',img)
#
# #cv2.imwrite('lenaC.png', img)
#
# cv2.waitKey(3000)
# cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()