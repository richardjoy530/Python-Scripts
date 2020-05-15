import socket			 
s = socket.socket()		 
s.connect(('192.168.18.10', 4042)) 
while True:
    print( s.recv(1024)) 
s.close()	 
