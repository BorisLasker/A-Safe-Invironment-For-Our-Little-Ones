
import os
import initial_ast
from ast_test import predict_sample_audio
import audio_test
import cam
from threading import Thread
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# from firebase import firebase
# firebase = firebase.FirebaseApplication("https://test-92470-default-rtdb.firebaseio.com/",None)

# data  = {
#     'name': 'boris'
    
# }

# result = firebase.post('https://test-92470-default-rtdb.firebaseio.com/user',data)

# print(result)
ADDRESS_FRAME_SAVE = 'audio'

def on_created(event):
   
        print(f"hey, {event.src_path} has been created!")
        try:
            if(predict_sample_audio(initial_ast.audio_model,initial_ast.labels,event.src_path)):
                #create_suspecious_video.Create_Vid(sample_audio_path,100)
                print(True)
        except Exception as e:
            print(e.args)

def AST():
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_created = on_created
    path = ADDRESS_FRAME_SAVE
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
                        
cam.Camera().start()

T_audio = audio_test.AudioSample().start()

Thread(target = AST(), args=()).start()


