import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(24, GPIO.OUT)  #LED to GPIO24

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

print('Button Pressed...' + current_time)

try:
    while True:
        button_state = GPIO.input(23)
        if button_state == False:
            GPIO.output(24, True)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print('Button Pressed...' + current_time)
            time.sleep(0.2)
        else:
            GPIO.output(24, False)
except:
    GPIO.cleanup()