import RPi.GPIO as GPIO
import time
import sys

def bin2dec(string_num):
    return str(int(string_num, 2))
   
data = []
effectiveData = []
bits_min=999;
bits_max=0;
HumidityBit = ""
TemperatureBit = ""
crc = ""
crc_OK = False;
Humidity = 0
Temperature = 0
pin=4

GPIO.setmode(GPIO.BCM)

def pullData():
    global data
    global effectiveData
    global pin
    
    data = []
    effectiveData = []
    
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(0.025)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(0.14)
    
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    for i in range(0,1000):
        data.append(GPIO.input(pin))
        
def analyzeData():
    seek=0;
    bits_min=9999;
    bits_max=0;

    global HumidityBit
    global TemperatureBit
    global crc
    global Humidity
    global Temperature

    HumidityBit = ""
    TemperatureBit = ""
    crc = ""
    
    while(seek < len(data) and data[seek] == 0):
        seek+=1;
    
    while(seek < len(data) and data[seek] == 1):
        seek+=1; 
        for i in range(0, 40):
            buffer = "";
            while(seek < len(data) and data[seek] == 0):
                seek+=1;
            
            while(seek < len(data) and data[seek] == 1):
                seek+=1;
                buffer += "1";    
            
            if (len(buffer) < bits_min):
                bits_min = len(buffer)
            
            if (len(buffer) > bits_max):
                bits_max = len(buffer)
            
            effectiveData.append(buffer);

    for i in range(0, len(effectiveData)):
        if (len(effectiveData[i]) < ((bits_max + bits_min)/2)):
            effectiveData[i] = "0";
        else:
            effectiveData[i] = "1";
    for i in range(0, 8):
        HumidityBit += str(effectiveData[i]);
    
    for i in range(16, 24):
        TemperatureBit += str(effectiveData[i]);
    
    
    for i in range(32, 40):
        crc += str(effectiveData[i]);
    
    Humidity = bin2dec(HumidityBit)
    Temperature = bin2dec(TemperatureBit)



def isDataValid():
    
    global Humidity
    global Temperature
    global crc
    
    print("isDataValid(): H=%d, T=%d, crc=%d"% (int(Humidity), int(Temperature), int(bin2dec(crc))))
    if int(Humidity) + int(Temperature) == int(bin2dec(crc)):
        return True;
    else:
        return False;
def printData():
    global Humidity
    global Temperature
    
    print("H: "+Humidity)
    print("T: "+Temperature)
   
    
while (not crc_OK):
    pullData();
    analyzeData();
    if (isDataValid()):
        crc_OK=True;
        print("\r", end=' ')
        printData();
    else:
        sys.stderr.write(".")
        time.sleep(2);
