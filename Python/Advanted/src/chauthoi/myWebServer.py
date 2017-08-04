#! usr/bin/python 2.7
import socket
import cgi

host=''
port=7777

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(1)

print 'Listen on port %s',port

while True:
    con, addr = s.accept()
    request=con.recv(1024)
    print request
    respone='Xin chao'

    con.sendall(bytes(respone(utf-8)))
    con.close()
