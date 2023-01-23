import os
import initial_ast
from ast_test import predict_sample_audio
import audio_test
import cam
from threading import Thread
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import create_suspecious_video
import connect_to_fb
from time import sleep
import VideoWithAudio

ADDRESS_SAVE = 'audio'
ADDRESS_VIDEO = 'saved videos'
ADDRESS_VideoWithAudio = 'VideoWithAudio'
ADDRESS_FRAME_SAVE = "saved frames/"

lastAudio = ' '

def on_created(event):
        global lastAudio
        print(f"{event.src_path}")
        try:
            if(predict_sample_audio(initial_ast.audio_model,initial_ast.labels,event.src_path)):
                currentAudio = event.src_path[6:]
                suspeciousObj = create_suspecious_video.Create_Vid(currentAudio,300,15)
                if lastAudio == ' ':
                    lastAudio = currentAudio
                    suspeciousObj.create_video()
                    
                if(suspeciousObj.delta_two_time(lastAudio) > 10):
                    suspeciousObj.create_video()
                    lastAudio = currentAudio
        except Exception as e:
            pass

def ast():
    print("Ast is listening for sounds...")
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_created = on_created
    path = ADDRESS_SAVE
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
        
        
        


if not os.path.exists(ADDRESS_SAVE):
    os.makedirs(ADDRESS_SAVE)
if not os.path.exists(ADDRESS_VIDEO):
    os.makedirs(ADDRESS_VIDEO)
if not os.path.exists(ADDRESS_VideoWithAudio):
    os.makedirs(ADDRESS_VideoWithAudio)
if not os.path.exists(ADDRESS_FRAME_SAVE):
    os.makedirs(ADDRESS_FRAME_SAVE)
    
    
VideoWithAudio.init_video_sound() 
 
connect_to_fb.ConnectToDB()
          
cam.Camera().start()

audio_test.AudioSample().start()

ast()

