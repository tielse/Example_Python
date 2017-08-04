#! usr/bin/python 2.7
import socket
import time
import threading

lock=threading.Lock()
shutdown=False
def receving(name, sock):
    while not shutdown:
        try:
            lock.acquire()
            while True:
                data, add = sock.recvfrom(1024)
                print str(data)
        except:
            pass
        else:
            lock.release()
host='127.0.0.1'
port=0

server=('127.0.0.1',443)
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

rT=threading.Thread(target=receving, args=("Receving",s))
rT.start()

tiroot=raw_input('Name: ')
msg=raw_input(tiroot+"-> ")
while msg != 'q':
    if msg!='':
        s.sendto(tiroot+": "+msg,server)
    lock.acquire()
    msg=raw_input(tiroot+'-> ')
    lock.release()
    time.sleep(0.2)

shutdown=True
rT.join()
s.close()
