
from socket import  *

socket = socket(AF_INET, SOCK_STREAM)
socket.connect( ('', 1234))

read = socket.recv(1024)
print('server:', read)

while True:
    msg = input(">")
    if msg == "exit":
        break
    read = socket.recv(1024)
    print('server:', read.decode('utf-8'))
    socket.send( (msg+"\n").encode('utf-8'))
    
socket.close()



