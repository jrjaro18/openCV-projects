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
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 13, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 13, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (cx, cy), 13, (0, 0, 255), cv2.FILLED)
        cv2.line(img, (x2, y2), (x1, y1), (0, 255, 255), 5)

        length = math.hypot(x2 - x1, y2 - y1)

        if(length<50):
            keyboard.press_and_release('Up')
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = time.time()
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, cv2.COLOR_Luv2RGB, 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)