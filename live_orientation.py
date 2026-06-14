import cv2
cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   # gray = cv2.GaussianBlur(gray, (5,5), 0)
    _,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:

        area = cv2.contourArea(contour)
        if area > 1000:
            rect = cv2.minAreaRect(contour)
            angle = rect[-1]
            if angle < -45:
                angle = 90 + angle
            angle = abs(angle)
            cv2.drawContours(frame,[contour],-1,(0,255,0),2)
            x, y, w, h = cv2.boundingRect(contour)

            cv2.putText(frame,f"Angle: {angle:.1f}",(x, y-10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    cv2.imshow("Live Orientation Detection",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
