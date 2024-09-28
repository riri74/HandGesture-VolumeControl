import cv2 as cv
import numpy as np
import time
import handtrackingmodule as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


#######################################
wCam , hCam = 640,480
#######################################


cap = cv.VideoCapture(0)
cap.set(3,  wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.handdetector(detectionConfidence=0.7)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
volRange = volume.GetVolumeRange()

minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400




while True:
    isTrue, img = cap.read()
    img = detector.findHands(img) # detects the hands
    lmlist = detector.findPosition(img, draw = False) # gives the postition of the hand
    if len(lmlist) != 0:
        #print(lmlist)

        x1,y1 = lmlist[4][1], lmlist[4][2]
        x2,y2 = lmlist[8][1], lmlist[8][2]
        cx,cy = (x1 + x2)//2 , (y1 + y2)//2 # center of the line

        cv.circle(img, (x1, y1), 10, (255, 0, 0), cv.FILLED) # puts a circle on thumb
        cv.circle(img, (x2, y2), 10, (255, 0, 0), cv.FILLED) # puts a cricle on index finger
        cv.line(img, (x1, y1), (x2,y2), (255, 0, 0), 2) #draws a line between the 2 fingers
        cv.circle(img, (cx, cy), 10, (255, 0, 255), cv.FILLED) # draws a circle at the center of the line

        length = math.hypot(x2 - x1, y2 - y1) # length of the line
        #print(length)

        # hand range 50 to 300
        # volume range -96 to 0
        # do note that the length of the line changes depending on the distance of the camera

        vol = np.interp(length, [50, 300], [minVol, maxVol])
        volBar = np.interp(length, [50, 300], [400, 150])
        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)


        if length < 50:
            cv.circle(img, (cx, cy), 10, (0, 255, 0), cv.FILLED) # changes the circle color to green

    # to show the volume on the side
    cv.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
    cv.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv.FILLED)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime 

    cv.putText(img, f'FPS: {int(fps)}', (30, 30), cv.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)


    cv.imshow('vid',img)
    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()