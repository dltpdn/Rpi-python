import wiringpi, time

wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(18, True)

while True:
    wiringpi.digitalWrite(18, True)
    time.sleep(0.5)
    wiringpi.digitalWrite(18, False)
    time.sleep(0.5)
    