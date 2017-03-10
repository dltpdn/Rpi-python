import RPi.GPIO as GPIO

try:
    pin = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    val = -1
    while True:
        read = GPIO.input(pin)
        if read != val:
            val = read
finally:
    print "clean up."
    GPIO.cleanup()
