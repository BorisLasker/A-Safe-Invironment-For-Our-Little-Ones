
import moviepy.editor as mpe
import ffmpeg
import threading
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import time
from threading import Thread
import os
import datetime as dt


ADDRESS_AUDIO = 'audio'
ADDRESS_VIDEO = 'saved videos'

def on_created(event):
   
        # print(f", {event.src_path}")
        videoName = event.src_path[13:-4]
        try:
            for root, dirs, files in os.walk(ADDRESS_AUDIO):
                for _file in files:
                    audioName = str(_file)
                    audioName = audioName[0:19]
                    print(audioName)
                    temp = audioName
                    temp1 =dt.datetime.strptime(temp,"%Y-%m-%d %H-%M-%S")
                    print(temp1)
                    temp1=temp1.seconds
                    print(temp1)
                    print('Here  '+ videoName,audioName)
                    if videoName == audioName:
                        combine_audio(videoName,audioName)  
        except Exception as e:
            print(e.args)


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
    vidname = ADDRESS_VIDEO + '/'+vidname+'.mp4'
    audname = ADDRESS_AUDIO + '/'+audname+'.wav'
    print("video "+vidname,"Audio " +audname)
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile('./VideoWithAudio/'+vidname[13:], fps=23, threads=1, codec="libx264")

def init_video_sound():
    Thread(target = create_video_with_sound).start()
init_video_sound()