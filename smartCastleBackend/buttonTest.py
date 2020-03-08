import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(24, GPIO.OUT)  #LED to GPIO24

now = datetime.now()
current_time = now.strftime("%Y.%M.%D %H:%M:%S")

print('Button Pressed...' + current_time)
oldButtonState = True

try:
    while True:
        button_state = GPIO.input(23)
        if oldButtonState != button_state:
            oldButtonState = button_state
            if button_state == False:
                GPIO.output(24, True)
                now = datetime.now()
                current_time = now.strftime("%Y.%M.%D %H:%M:%S")
                print('Button Pressed...' + current_time)
            else:
                GPIO.output(24, False)
        time.sleep(0.2)
except:
    GPIO.cleanup()