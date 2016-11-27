import RPi.GPIO as GPIO
import time

pin = 25
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    p = GPIO.PWM(pin,100)
    p.start(5)
    while True:
        p.ChangeDutyCycle(5) #-90degree
        time.sleep(1)
        p.ChangeDutyCycle(15) #0 dgree
        time.sleep(2)
        p.ChangeDutyCycle(25) #+90 degree
        time.sleep(1)
        p.ChangeDutyCycle(15) #0 dgree
        time.sleep(2)
except KeyboardInterrput:
    p.stop()
    GPIO.cleanup()
