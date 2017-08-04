#! usr/bin/pythion 2.7
import socket

def Main():
    host='127.0.0.1'
    port=443
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))

    s.listen(1)
    c, add=s.accept()
    print 'Ket noi thanh cong!',str(add)
    while True:
        data=c.recv(1024)
        if not data:
            break
        print 'ket noi den user: ',str(data)
        data=str(data).upper()
        print 'sending: ',str(data)
        c.send(data)

    c.close()
if __name__ == '__main__':
    Main()