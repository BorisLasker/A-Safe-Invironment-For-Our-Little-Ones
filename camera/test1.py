
import cv2
import os
import time
import datetime as dt
ADDRESS_FRAME_SAVE = "camera/saved frames/"
ADDRESS_VIDS_SAVE = "camera/saved vids/"
counter =0
import imutils
import create_suspecious_video
import cam


# t=str(time.strftime("%Y%m%d%H%M-%S"))
# print(type(t))
# os.rename(ADDRESS_FRAME_SAVE+'0--.jpg',ADDRESS_FRAME_SAVE+t+str(counter)+'--.jpg')

# current_time = str(dt.datetime.now())
# current_time = current_time[:-7]
# print("==>> current_time: ", current_time)



# now = dt.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H-%M-%S"))
# str_1 = now.strftime("%Y-%m-%d %H-%M-%S")

# date1=dt.datetime.strptime(str_1,"%Y-%m-%d %H-%M-%S")

# print("==>> date1: ", date1)




# capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
# W, H = 640, 480
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, W)
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, H)
# capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
# capture.set(cv2.CAP_PROP_FPS, 50)
# vid_cod = cv2.VideoWriter_fourcc(*'mp4v')
# # output = cv2.VideoWriter("camera/saved videos/b1.mp4", vid_cod, 20, (640,480))
# while(True):
#      # Capture each frame of webcam video
     
#      ret,frame = capture.read()
    

#      cv2.imshow("My cam video", frame)
#     #  output.write(frame)
#      # Close and break the loop after pressing "x" key
#      if cv2.waitKey(1) &0XFF == ord('x'):
#          break
# # close the already opened camera
# capture.release()
# # close the already opened file
# # output.release()
# # close the window and de-allocate any associated memory usage
# cv2.destroyAllWindows()


import threading


sem = threading.Semaphore(1)

vid_len=1000

a=threading.Thread(target=create_suspecious_video.Create_Vid, args=('2022-11-12 12-08-12.wav', vid_len))
a.start()

b=cam.Camera().start()
print('done!')