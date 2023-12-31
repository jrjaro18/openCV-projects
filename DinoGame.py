from HandTrackingModule import HandDetector
import cv2
import mediapipe as mp
import time
import keyboard
import math

ptime = 0
ctime = 0
cap = cv2.VideoCapture(0)
detector = HandDetector()
prev = 210
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    liList = detector.findPosition(img)
    if len(liList) != 0:
        x1, y1 = liList[4][1], liList[4][2]
        x2, y2 = liList[8][1], liList[8][2]
        x3, y3 = liList[12][1], liList[12][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        mx, my = (x1+x3) // 2 , (y1+y3) // 2

        cv2.circle(img, (x1, y1), 7, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 7, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (cx, cy), 7, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (mx, my), 7, (0, 0, 255), cv2.FILLED)
        cv2.line(img, (x2, y2), (x1, y1), (0, 255, 255), 5)
        cv2.line(img, (x3, y3), (x1, y1), (0, 255, 255), 5)


        length1 = math.hypot(x2 - x1, y2 - y1)
        length2 = math.hypot(x3 - x1, y3 - y1)

        if(length1<50):
            keyboard.press_and_release('Up')
        if (length2 < 50):
            keyboard.press_and_release('Down')
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = time.time()
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, cv2.COLOR_Luv2RGB, 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)