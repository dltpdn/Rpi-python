
from socket import  *

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(('', 1234))
server.listen(1)
print("server listening on 1234...")
conn, addr = server.accept()

conn.send(b'Welcome to python tcp server.')
while True:
    msg = input(">")
    if msg == "exit":
        break
    conn.send( (msg+"\n").encode('utf-8'))
    read = conn.recv(1024)
    print('client:', read.decode('utf-8'))
    
conn.close()

