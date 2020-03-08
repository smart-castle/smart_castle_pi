import secrets
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("smartcastlebase-firebase-adminsdk.json")
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smartcastlebase.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('users/' + secrets.uid + '/devices/' + secrets.did + '/services/' + secrets.sid)
ref.set({
    'isOpen': 'false',
    'name': 'Door open sensor',
    'type': '1',
    'nr': '1',
})
print(ref.get())


# "users": {
#       "$uid": {
#         ".read": "$uid === auth.uid",
#         ".write": "$uid === auth.uid"
#       }
#     }