import cv2
import time
from handTrackingModule import handDetector  # Ensure this module is correctly imported

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.detector = handDetector(detectionCon=0.75)
        self.wcam, self.hcam = 640, 480
        self.video.set(3, self.wcam)
        self.video.set(4, self.hcam)
        self.pTime = 0

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()
        if not ret:
            return None

        img = self.detector.findHands(frame, draw=True)
        lmList = self.detector.findPosition(img, draw=False)
        tipId = [4, 8, 12, 16, 20]

        if len(lmList) != 0:
            fingers = []
            # Thumb
            if lmList[tipId[0]][1] > lmList[tipId[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            # 4 fingers
            for id in range(1, len(tipId)):
                if lmList[tipId[id]][2] < lmList[tipId[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            
            cv2.rectangle(img, (20, 255), (170, 425), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, str(self.getNumber(fingers)), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                        10, (255, 0, 0), 20)

        cTime = time.time()
        fps = 1 / (cTime - self.pTime)
        self.pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 3)
        
        ret, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tobytes()

    def getNumber(self, fingers):
        return sum(fingers)
