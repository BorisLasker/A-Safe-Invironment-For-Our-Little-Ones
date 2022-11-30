import datetime as dt
import os
import shutil
import numpy as np
import cv2

ADDRESS_FRAME_SAVE = "saved frames/"
ADDRESS_VIDEO_SAVE = 'saved videos/'

class Create_Vid:
 

    def __init__(self, date, vid_len,delta):
        self.date = date
        self.date = self.date[:-4]
        self.vid_len = vid_len
        self.delta = delta
        self.date = self.delta_time(delta)
        #self.merge_frames()
        
    def delta_time(self,delta):
        date1=dt.datetime.strptime(self.date,"%Y-%m-%d %H-%M-%S")  
        date1 = date1 - dt.timedelta(seconds=int(delta))
        date1=dt.datetime.strftime(date1,"%Y-%m-%d %H-%M-%S")  
        return (date1)
    
    def delta_two_time(self,date2):
            date2 = date2[:-4]
            date1=dt.datetime.strptime(self.date,"%Y-%m-%d %H-%M-%S") 
            
            print(date1)
            date2=dt.datetime.strptime(date2,"%Y-%m-%d %H-%M-%S")  
            
            date = date2- date1
            return ( date.seconds)
        
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

# vid_len=250
# def CreateVideo(suspecious_sound):
#      delta = 10
#      a = Create_Vid(suspecious_sound,vid_len,delta )

