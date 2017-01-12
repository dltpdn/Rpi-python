import bluetooth as bt

socket = bt.BluetoothSocket( bt.RFCOMM )

socket.connect(("B8:27:EB:AD:74:74", 3)) # change to target address
print "connected."
socket.send("Hello Bluetooth World.")
print "sent data"
recv = socket.recv(1024)
print "recv data : %s" % recv

socket.close()