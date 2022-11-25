
import cv2
import os
import time
import WebcamVideoStream
from threading import Thread
global FlagMicStop
FlagMicStop = False

class Camera:

    def __init__(self):
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





# vs = WebcamVideoStream.WebcamVideoStream(src=0).start()

# counter = 0

# while True:
#     image = vs.read()
#     cv2.imshow('Image', image)
#     counter+=1
#     cv2.imwrite(ADDRESS_FRAME_SAVE+time.strftime("%Y-%m-%d %H-%M-%S---")+'{:06}'.format(counter)+'.jpg',image)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#       break
#     time.sleep(0.025)

# vs.stop()
# cv2.destroyAllWindows()

# print(counter)








# import cv2
# camera=0
# cap = cv2.VideoCapture(camera, cv2.CAP_DSHOW)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)

# out = cv2.VideoWriter('camera/saved videos/a1.mp4', cv2.VideoWriter_fourcc(*"mp4v"), 20.0, (1920,1080))

# while cap.isOpened():
#     success, image = cap.read()
#     if not success:
#       continue
#     cv2.imshow('Image', image)
#     out.write(image)
#     if cv2.waitKey(5) & 0xFF == ord("q"):
#       break
# cap.release()



