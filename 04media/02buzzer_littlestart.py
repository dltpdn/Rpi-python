import wiringpi  
from time import sleep  
pin = 24
frequencies = {'c':262, 'd':294, 'e':330, 'f':349, 'g':392, 'a':440, 'b':494}
notes = 'ccggaag ffeeddc ggffeed ggffeed ccggaag ffeeddc'

wiringpi.wiringPiSetupGpio()  
  
try:
    wiringpi.softToneCreate(pin)
    for i in notes:
        if i != ' ':
            wiringpi.softToneWrite(pin, frequencies[i])
        sleep(0.3)
finally:
    wiringpi.pinMode(pin, 0)
