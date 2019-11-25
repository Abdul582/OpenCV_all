import cv2

cap = cv2.VideoCapture('vtest.avi')

res, frame1 = cap.read()
res, frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilate = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #cv2.drawContours(frame1, contours, -1, (0,255,0),2)

    for contours in contours:
        (x, y, h, w) = cv2.boundingRect(contours)

        if cv2.contourArea(contours) < 700:
            continue
        cv2.rectangle(frame1,(x,y), (x+h, y+w), (0,255,0), 2)
        cv2.putText(frame1, 'Status : {}'.format('MOvement'), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)




    cv2.imshow('feed', frame1)
    frame1 = frame2
    ret, frame2 = cap.read()
    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()

