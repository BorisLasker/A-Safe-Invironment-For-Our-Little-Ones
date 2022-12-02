
import cv2
import os
import time
import WebcamVideoStream
from threading import Thread
global FlagMicStop
FlagMicStop = False

class Camera:

    def __init__(self):
      print("Camera is on")
      self.counter = 0
      
    def start(self):
        # start the thread to read frames from the video stream
        
        Thread(target=self.cameraRecord, args=()).start()
        return self
      
    
    def cameraRecord(self):
        # start the thread to read frames from the video stream
        self.vs = WebcamVideoStream.WebcamVideoStream(src=0).start()
        while True:
            self.image = self.vs.read()
            cv2.imshow('Image', self.image)
            self.counter+=1
            cv2.imwrite(ADDRESS_FRAME_SAVE+time.strftime("%Y-%m-%d %H-%M-%S---")+'{:06}'.format(self.counter)+'.jpg',self.image)
            if cv2.waitKey(1) & 0xFF == ord("q"):
              global  FlagMicStop
              FlagMicStop = True
              break
            time.sleep(0.025)

        self.vs.stop()
        cv2.destroyAllWindows()

        print(self.counter)



ADDRESS_FRAME_SAVE = "saved frames/"

# cam=Camera().start()
