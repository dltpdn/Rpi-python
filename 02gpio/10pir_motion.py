import RPi.GPIO as GPIO 
import time
from datetime import datetime

pri_pin = 18
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pri_pin, GPIO.IN)
    val = -1
    while True:
        read = GPIO.input(pri_pin)
        if val != read: 
            val = read
            if val== 0:
                print(str(datetime.now()), "No intruder")
            elif val == 1:
                print(str(datetime.now()), "Intruder dectected")
        time.sleep(0.5)
finally:
    print('clean up')
    GPIO.cleanup() 
