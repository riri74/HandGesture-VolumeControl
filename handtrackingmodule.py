# get position of the landmarks

import cv2 as cv
import mediapipe as mp
import time 


class handdetector():
    def __init__(self, mode = False, maxHands = 2, detectionConfidence = 0.5, trackConfidence = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, 
                                max_num_hands=self.maxHands, 
                                min_detection_confidence=self.detectionConfidence, 
                                min_tracking_confidence=self.trackConfidence)

        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw = True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        #print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks: 
                    if draw:
                        self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
    
    def findPosition(self, img, handNum = 0, draw = True):
        
        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNum]            

            for id, lm in enumerate(myHand.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                #print(id, cx, cy)
                lmlist.append([id,cx,cy])
                if draw:
                    cv.circle(img, (cx, cy), 5, (255, 0, 255), cv.FILLED)
        return lmlist
    




    



def main(): # dummy tool that'll tell what this module can do
    pTime = 0 
    cTime = 0 
    cap = cv.VideoCapture(0)
    detector = handdetector( )
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmlist = detector.findPosition(img)
        if len(lmlist) != 0:
            print(lmlist[4])
        
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        
        #cv.putText(img, str(int(fps)), (10, 17), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)


        cv.imshow('image',img) # displays the window with name image
        cv.waitKey(1) # waits fr 1ms for a key press on the window






if __name__ == "__main__": # checks if we're running this script
    main()