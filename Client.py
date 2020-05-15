import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('196.168.18.10', 80))


while True:
    msg = s.recv(24)
    if len(msg) <= 0:
        break
    print(msg)

s.close()


    