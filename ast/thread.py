from firebase_admin import credentials, initialize_app, storage
import threading
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db 
from firebase_admin import credentials, initialize_app, storage

from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import time
from threading import Thread
ADDRESS_FRAME_SAVE = 'saved videos'

# Init firebase with your credentials
cred = credentials.Certificate("firebase-sdk.json")
initialize_app(cred, {
    'storageBucket': 'mediashare-72f12.appspot.com',
    'databaseURL': 'https://mediashare-72f12-default-rtdb.firebaseio.com/'
    })

# Put your local file path 
fileName = "2022-11-29 18-55-32.mp4"
bucket = storage.bucket()
blob = bucket.blob(fileName)
blob.upload_from_filename(fileName)

# Opt : if you want to make public access from the URL
blob.make_public()

print("your file url", blob.public_url)

# firebase_admin.initialize_app(cred,{
#         'databaseURL': 'https://mediashare-72f12-default-rtdb.firebaseio.com/'
#     })

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
ref = db.reference('message')
user_ref = ref.push({
                'currentDateTime':dt_string,     
                'email':"boris.laskerr@gmail.com",
                'imageUrl': blob.public_url,
                'username':"Bor La"
            })




 

 
 
 