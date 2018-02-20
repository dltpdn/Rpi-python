import serial

port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=3.0)
try:
    if port.isOpen():
        print('serial writer is ready.')
    
    while True:
        line = input(">")
        print(line)
        port.write(line + '\n\r')
finally:
    port.close() 