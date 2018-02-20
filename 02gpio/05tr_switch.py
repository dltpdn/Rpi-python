import RPi.GPIO as GPIO

pin = 18

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    
    while True:
        val = eval(input("1:on, 0:off"))
        GPIO.output(pin, val)
finally:
    print('clean up')
    GPIO.cleanup()
