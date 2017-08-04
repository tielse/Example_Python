#! usr/bin/python 2.7

import socket

def MainUDP():

    host='127.0.0.1'
    port=5000

    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))

    print 'Bat dau ket noi!'
    while True:
        data,add = s.recvfrom(1024)
        print 'Gui tin thanh cong: ',str(add)
        print 'Ket noi voi user: ',str(data)

        data=str(data).upper()
        s.sendto(data,add)
    s.close()

if __name__ == '__main__':
   MainUDP()