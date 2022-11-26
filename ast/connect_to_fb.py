import firebase_admin
from firebase_admin import credentials
from firebase_admin import db 

cred = credentials.Certificate("firebase-sdk.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://mediashare-72f12-default-rtdb.firebaseio.com/'
})
ref = db.reference('User')
user_ref = ref.push({
                      
    'email':"boris.laskerr@gmail.com",
    'password':"123",
    'username':"Bor La"

 })
