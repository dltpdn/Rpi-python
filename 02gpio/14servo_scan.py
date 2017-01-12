

import RPi.GPIO as GPIO
import time

pin = 25
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    #p = GPIO.PWM(pin,50)
    p = GPIO.PWM(pin,100)
    degree = 15;
    gap = 0.11 #1degree : 0.1111
    direction = True;
    p.start(degree)
    while True:
        if direction == True:
            if degree < 25:
                degree += gap
            else :
                degree = 25 - gap
                direction = False
        else:
            if degree > 5:
                degree -= gap
            else:
                degree = 5 + gap
                direction = True
        p.ChangeDutyCycle(degree)
        time.sleep(0.01)
except KeyboardInterrput:
    p.stop()
    GPIO.cleanup()