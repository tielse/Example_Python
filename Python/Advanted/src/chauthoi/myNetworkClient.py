#! usr/bin/python 2.7

import socket

def Main():
    host='127.0.0.1'
    port=443

    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host,port))

    msg=raw_input("-> ")
    while msg != 'q':
        s.send(msg)
        data=s.recv(1024)
        print 'Ket thanh cong den server: ',str(data)
        msg=raw_input("-> ")
    s.close()

if __name__ == '__main__':
    Main()