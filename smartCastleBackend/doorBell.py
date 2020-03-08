import RPi.GPIO as GPIO
import time
from datetime import datetime
import secrets
import firebase_admin
from firebase_admin import credentials, db

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(24, GPIO.OUT)  #LED to GPIO24

cred = credentials.Certificate("smartcastlebase-firebase-adminsdk.json")
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smartcastlebase.firebaseio.com/'
})

ref = db.reference('users/' + secrets.uid + '/devices/' + secrets.did + '/services/' + secrets.sid)
refData = db.reference('users/' + secrets.uid + '/devices/' + secrets.did + '/services/' + secrets.sid + '/data/')


oldButtonState = True

try:
    while True:
        button_state = GPIO.input(23)
        if oldButtonState != button_state:
            oldButtonState = button_state
            if button_state == False:
                GPIO.output(24, True)
                setData(button_state)
            else:
                GPIO.output(24, False)
                setData(button_state)
        time.sleep(2)
except:
    GPIO.cleanup()



def setData(open):
    now = datetime.now()
    current_time = now.isoformat()
    print(current_time + ': Door status changed new Status:' + open)
    refData.set({
        current_time: open
    })