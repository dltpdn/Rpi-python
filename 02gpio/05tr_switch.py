    pin = 18
    
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        
        while True:
            val = input("swtich [on:1, off:0]")
            GPIO.output(pin, val)
    finally:
        print 'clean up'
        GPIO.cleanup()
