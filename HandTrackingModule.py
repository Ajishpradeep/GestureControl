import os
import cv2
import numpy as np
from win32api import GetSystemMetrics
from cvzone.HandTrackingModule import HandDetector

# print("Width =", GetSystemMetrics(0))
# print("Height =", GetSystemMetrics(1))

width, height = GetSystemMetrics(0) , GetSystemMetrics(1)
# print (width, height)
# FolderPath1 = "Presentation1"
FolderPath = "Presentation"
cap = cv2.VideoCapture(0)
cap.set (3, width)
cap.set (4, height)

pathImages = sorted(os.listdir(FolderPath), key=len)
# print(pathImages)
imgNumber = 0
hs,ws  = int (120*1.5), int(213*1.5)
gestureThreshold = int(height/1.9)
buttonPressed =False
buttonCounter =0
buttonDelay = 30
annotations = [[]]
annotationNumber =-1
annotationStart = False
detector = HandDetector(detectionCon=0.8, maxHands=1)


while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    pathFullImages =os.path.join(FolderPath,pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImages)
    hands, img = detector.findHands(img)
    cv2.line(img ,(0,gestureThreshold), (width,gestureThreshold),(0,255,0),1)



    if hands and buttonPressed is False:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        cx , cy = hand['center']
        lmList = hand['lmList']
        indexFinger = lmList[8][0],lmList[8][1]
        xVal = int(np.interp(lmList[8][0], [width//2, w], [0,width]))
        yVal = int(np.interp(lmList[8][1], [150, height -150], [0, height]))
        indexFinger = xVal, yVal


        # print(fingers)
        if cy <=gestureThreshold:
            if fingers == [1,0,0,0,0]:
                print("Left")

                if(imgNumber>0):
                    buttonPressed = True
                    annotations = [[]]
                    annotationNumber = -1
                    annotationStart = False
                    imgNumber -= 1
            if fingers == [0,1,1,0,0]:
                print("Right")

                if(imgNumber<len(pathImages)-1):
                    buttonPressed = True
                    annotations = [[]]
                    annotationNumber = -1
                    annotationStart = False
                    imgNumber += 1

        if fingers == [0,1,0,0,0]:
             cv2.circle(imgCurrent,indexFinger, 5, (0,0,255),cv2.FILLED)

    if buttonPressed:
        buttonCounter += 1
        if buttonCounter > buttonDelay:
            buttonCounter = 0
            buttonPressed = False


    imgSmall = cv2.resize (img , (ws,hs))
    h,w,_ = imgCurrent.shape
    imgCurrent[0:hs, w-ws:w] = imgSmall
    cv2.imshow("Image", img)
    cv2.imshow("Presentation", imgCurrent)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

