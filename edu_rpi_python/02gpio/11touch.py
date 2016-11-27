import time
import datetime
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

pad_pin = 5
GPIO.setup(pad_pin, GPIO.IN)

while True:
    pad_pressed = GPIO.input(pad_pin)

    if pad_pressed:
        current_datetime = datetime.datetime.now().strftime("%I:%M%p:%S on %B %d, %Y")
        print("pressed! - " + current_datetime)

    time.sleep(0.1)
