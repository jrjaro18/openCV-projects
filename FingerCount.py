from HandTrackingModule import HandDetector
import cv2
import mediapipe as mp
import time
import os

ptime = 0
ctime = 0
cap = cv2.VideoCapture(0)
handImg = os.listdir('assets/fingers')
handImgList = []
for x in handImg:
    image = cv2.imread('assets/fingers'+'/'+x)
    handImgList.append(image)

print(handImgList)
detector = HandDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    liList = detector.findPosition(img, draw=False)
    if len(liList) != 0:
        count = 0
        if (liList[8][2] < liList[5][2]):
            count+=1
        if(liList[12][2] < liList[9][2]):
            count+=1
        if (liList[16][2] < liList[13][2]):
            count+=1
        if(liList[20][2] < liList[17][2]):
            count+=1
        if(liList[1][1] < liList[4][1]):
            count+=1
        img[:200,:200] = handImgList[count]

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = time.time()
    cv2.putText(img, str(int(fps)), (500, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, cv2.COLOR_Luv2RGB, 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)