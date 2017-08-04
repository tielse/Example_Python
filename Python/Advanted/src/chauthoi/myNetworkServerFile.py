#! usr/bin/python 2.7
import socket
import os
import threading

def RFile():
    filename=socket.recv(1024)
    if os.path.isfile(filename):
        socket.send("EXIT",str(os.path.getsize(filename)))
        usrResponse=socket.recv(1024)
        if usrResponse[:2] == 'OK':
            with open(filename,'rb') as f:
                byteSend=f.recv(1024)
                socket.send(byteSend)
                while byteSend!="":
                    byteSend=f.read(1024)
                    sock.send(byteSend)
        else:
            socket.send('Error')

        socket.close()
def Main():
    host='127.0.0.1'
    port=443

    s=socket.socket()
    s.bind((host,port))
    s.listen(5)

    print 'Start server'
    while True:
        c, add=s.accept()
        print 'Client connection ip:<'+str(add)+'>'
        t=threading.Thread(target=RFile(), args=("RThread",c))
        t.start()

    s.close()

if __name__ == '__main__':
    Main()