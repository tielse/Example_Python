#! usr/bin/python 2.7
import socket

def Main():
    host='127.0.0.1'
    port=443
    s=socket.socket()
    s.connect((host,port))

    filename=raw_input('File name: ->')

    if filename != 'q':
        s.send(filename)
        data=s.recv(1024)
        if data[:6]== 'EXIT':
            filesize=long(data[:6])
            msg=raw_input('File exits: ',str(filesize)+'Byte, load? (Y/N)')
            if msg == 'Y':
                s.send('OK')
                f=open('new'+filename+'wb')
                data=s.recv(1024)
                totalR=len(data)
                f.write(data)
                while totalR < filesize:
                    data=s.recv(1024)
                    totalR+=len(data)
                    f.write(data)
                    print '{0:.2f}'.format((totalR/float(filesize))*100)+'% Done'
                print "Download complete!"
        else:
            print 'File dose not Exits'
    s.close()

if __name__ == '__main__':
    Main()