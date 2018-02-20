
from socket import  *
import threading

running = True

def recv():
    while running:
        read = conn.recv(1024)
        print('client:', read.decode('utf-8'))

try:
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind(('', 1234))
    server.listen(1)
    print("server listening on 1234...")
    conn, addr = server.accept()
    th = threading.Thread(target=recv)
    th.start()
    conn.send(b'Welcome to python tcp server.')
    
    while running:
        msg = input(">")
        if msg == "exit":
            break
        conn.send( (msg+"\n").encode('utf-8'))
    
    conn.close()
finally:
    running = False
