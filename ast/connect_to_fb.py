# import firebase_admin
# from firebase_admin import credentials

# cred = credentials.Certificate("path/to/serviceAccountKey.json")
# firebase_admin.initialize_app(cred)

import firebase_admin
from firebase_admin import auth, credentials, firestore, db
from firebase import firebase

# JSON_ADDRESS = "camera/firebase-config.json"

# cred = credentials.Certificate(JSON_ADDRESS)
# firebase_admin.initialize_app(cred,{
#     'databaseURL': 'https://mediashare-72f12-default-rtdb.firebaseio.com/'})
# db = firestore.client()
# ref = db.reference('/')
# collection = ref.collection('programmer_details')  # create collection
# res = collection.document('A01').set({ # insert document
#     'name': 'Vishnu',
#     'age': 19,
#     'Country': 'India',
#     'Programming_languages': ['Python', 'C#', 'C++']
# })
# print(res)

# ref = db.reference('/')
# ref.child('Employee').set(
#     {
#         'emp2':{
#             'name':'boris'
#         }

#     }
# )

firebase = firebase.FirebaseApplication("https://mediashare-72f12-default-rtdb.firebaseio.com/User",None)

data = {
    'name':'daniel'
}

# result = firebase.post('https://mediashare-72f12-default-rtdb.firebaseio.com/costumer',data)




