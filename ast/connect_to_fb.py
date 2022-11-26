import firebase_admin
from firebase_admin import credentials
from firebase_admin import db 

cred = credentials.Certificate("firebase-sdk.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://mediashare-72f12-default-rtdb.firebaseio.com/'
})
ref = db.reference('message')
user_ref = ref.push({
              
    'currentDateTime':"21 בנוב׳ 2022 10:19:21",     
    'email':"boris.laskerr@gmail.com",
    'imageUrl':"https://www.fao.org/images/devforestslibraries/default-album/forests.jpg?sfvrsn=2dd96b96_11",
    'username':"Bor La"

 })
