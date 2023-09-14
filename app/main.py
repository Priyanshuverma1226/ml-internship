import cv2
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    success,img=cap.read()
    print(img)
    cv2.imshow("Output",img)
    key=cv2.waitKey(1)