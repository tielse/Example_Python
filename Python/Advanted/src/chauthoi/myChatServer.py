#! usr/bin/python
import socket
import time

host='127.0.0.1'
port=443

clients=[]

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

print 'Ket noi server!'

while not quit:
    try:
        data, add = s.recvfrom(1024)
        if "Thoat" in str(data):
            quit=True
        if add not in clients:
            clients.append(add)

        print time.ctime(time.time())+str(add)+" : : "+str(data)
        for client in clients:
            s.sendto(data, client)
    except:
        pass
s.close()