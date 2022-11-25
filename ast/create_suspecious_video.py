import datetime as dt
import os
import shutil
import numpy as np
import cv2

ADDRESS_FRAME_SAVE = "saved frames/"
ADDRESS_VIDEO_SAVE = 'saved videos/'

class Create_Vid:
 

    def __init__(self, date, vid_len):
        self.date = date
        self.date = self.date[:-4]
        self.vid_len = vid_len
        
        self.merge_frames()
        
    def delta_time(self,delta):
        # current_time = dt.datetime.now()
        # current_time = current_time[:-7]
        
        date1=dt.datetime.strptime(self.date,"%Y-%m-%d %H-%M-%S")     
        return (date1 - dt.timedelta(seconds=int(delta)))

    def merge_frames(self):
        found = False
        out = cv2.VideoWriter(ADDRESS_VIDEO_SAVE+str(self.date)+'.mp4', cv2.VideoWriter_fourcc(*"mp4v"), 23 , (1280,720))
        for root, dirs, files in os.walk(ADDRESS_FRAME_SAVE):
            for _file in files:
                img_name = str(_file)
                img_name = img_name[0:19]
                if found:
                    self.vid_len -=1
                    if self.vid_len == 0:
                        break
                    img_path = os.path.join(ADDRESS_FRAME_SAVE, _file)
                    img = cv2.imread(img_path)
                    out.write(img)
                    continue
                if img_name==str(self.date):
                    found=True  
        out.release()

vid_len=100
a = Create_Vid('2022-11-12 12-08-11.wav', vid_len)
a.merge_frames()
















# current_time = dt.datetime.now()
# current_time.strftime("%Y-%m-%d %H-%M-%S")
