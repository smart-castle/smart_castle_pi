import time
from datetime import datetime
import secrets
import firebase_admin
from firebase_admin import credentials, db, messaging

cred = credentials.Certificate("smartcastlebase-firebase-adminsdk.json")
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smartcastlebase.firebaseio.com/'
})

ref = db.reference('users/' + secrets.uid + '/devices/' + secrets.did + '/services/' + secrets.sid)
refData = db.reference('users/' + secrets.uid + '/devices/' + secrets.did + '/services/' + secrets.sid + '/data/')

def setData(open):
    now = datetime.now().replace(microsecond=0)
    current_time = now.isoformat()
    print(current_time + ': Door status changed new Status:' + str(open))
    refData.set({
        current_time : str(open)
    })

def sendMessage():
    now = datetime.now().replace(microsecond=0)
    current_time = now.isoformat()
    note = firebase_admin.messaging.Notification(title='Door Alarm', body='Door was Opend at: ' + current_time, image=None)
    message = firebase_admin.messaging.Message(data=None, notification=note, android=None, webpush=None, apns=None, fcm_options=None, token=secrets.token, topic=None, condition=None)
    firebase_admin.messaging.send(message, dry_run=False, app=None)


setData(1)
sendMessage()



