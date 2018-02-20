
from socket import  *
import threading

running = True
def recv():
    while running:
        read = socket.recv(1024)
        print('client:', read.decode('utf-8'))

try:
    socket = socket(AF_INET, SOCK_STREAM)
    socket.connect(('', 1234))
    th = threading.Thread(target=recv)
    th.start()
    socket.send(b'Hi! This is a client.')
    
    while running:
        msg = input(">")
        if msg == "exit":
            break
        socket.send( (msg+"\n").encode('utf-8'))
        
    socket.close()
finally:
    running = False
