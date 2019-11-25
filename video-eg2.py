import cv2

cap = cv2.VideoCapture('output.avi')

while(cap.isOpened()):
    ret, frame = cap.read()
    cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    cv2.imshow('frame',frame)
    if cv2.waitKey() & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()