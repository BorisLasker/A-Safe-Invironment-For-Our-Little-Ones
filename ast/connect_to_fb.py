import threading
import firebase_admin
from firebase_admin import db 
from firebase_admin import credentials, initialize_app, storage

from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import time
from threading import Thread

ADDRESS = 'VideoWithAudio'

def on_created(event):
   
        print(f"hey, {event.src_path} a new video has been uploded!")
        try:
            fileName = event.src_path
            bucket = storage.bucket()
            blob = bucket.blob(fileName)
            blob.upload_from_filename(fileName)

            # Opt : if you want to make public access from the URL
            blob.make_public()
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            ref = db.reference('message')
            user_ref = ref.push({
                'currentDateTime':dt_string,     
                'email':"Admin",
                'imageUrl': blob.public_url,
                'username':"Admin"
            })
        except Exception as e:
            print(e.args)

def uploadSuspeciousVideo():
    print("Connected to Data Base")
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_created = on_created
    path = ADDRESS
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
        
        
        


def ConnectToDB():

    cred = credentials.Certificate("firebase-sdk.json")
    initialize_app(cred, {
        'storageBucket': 'mediashare-72f12.appspot.com',
        'databaseURL': 'https://mediashare-72f12-default-rtdb.firebaseio.com/'
        })
    Thread(target = uploadSuspeciousVideo).start()