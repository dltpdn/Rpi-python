import RPi.GPIO as GPIO 
import time
from datetime import datetime

trig_pin = 24
echo_pin = 23 
distance = 0
start_time = 0

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trig_pin, GPIO.OUT)
    GPIO.setup(echo_pin, GPIO.IN)
    
    while True:
        GPIO.output(trig_pin, False)
        print "ready for mesurement."
        time.sleep(0.2)
        GPIO.output(trig_pin, True)
        time.sleep(0.00001)  #set HIGH for 10us
        GPIO.output(trig_pin, False)
        while GPIO.input(echo_pin) == 0:
            start_time = time.time()
        while GPIO.input(echo_pin) == 1:
            end_time = time.time()
        travel_time = end_time - start_time;
        distance = travel_time * 17150 #32300/2
        distance = round(distance, 2)
        print 'Distance:%dcm' %distance
finally:
    print 'Clean up'
    GPIO.cleanup()                
