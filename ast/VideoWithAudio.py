
import moviepy.editor as mpe
import ffmpeg
import threading
from datetime import datetime, timedelta
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import time
from threading import Thread
import os
import datetime as dt
import shutil
ADDRESS_AUDIO = 'audio'
ADDRESS_VIDEO = 'saved videos'

def changeTime(tempTime,time):
    tempTime =dt.datetime.strptime(tempTime,"%Y-%m-%d %H-%M-%S")
    tempTime = tempTime + timedelta(hours=0, minutes=0, seconds=time)
    tempTime=dt.datetime.strftime(tempTime,"%Y-%m-%d %H-%M-%S") 
    return tempTime

def on_created(event):
        # time.sleep(1)
        videoName = event.src_path[13:-4]
        videoName = changeTime(videoName,15)
        try:
            for root, dirs, files in os.walk(ADDRESS_AUDIO):
                for _file in files:
                        audioName = str(_file)
                        audioName = audioName[0:19]
                        if videoName == audioName:
                            combine_audio(videoName,audioName)
                            raise StopIteration
        except Exception as e:
            print("videowithaudio")
        except StopIteration:
            pass


def create_video_with_sound():
    
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_created = on_created
    path = ADDRESS_VIDEO
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)
    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except Exception:
        my_observer.stop()
        my_observer.join()


def combine_audio(vidname, audname):
    vidname = changeTime(vidname,-15)
    vidname = ADDRESS_VIDEO + '/'+vidname+'.mp4'
    audname = ADDRESS_AUDIO + '/'+audname+'.wav'
    print("video "+vidname,"Audio " +audname)
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile('./'+vidname[13:], fps=23, threads=1, codec="libx264",verbose=False,  logger= None)
    shutil.move('./' + vidname[13:],'./VideoWithAudio')

def init_video_sound():
    Thread(target = create_video_with_sound).start()

