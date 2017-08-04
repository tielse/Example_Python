#!/usr/bin/env python 2.7
import optparse
import socket

from socket import *

def Connect(LHOST,LPORT):
    try:
        n=sorted(AF_INET,SOCK_STREAM)
        n.connect(LHOST,LPORT)
        n.send('Send\r\n')
        reslt=n.recv(100)
        print '[+]%d /TCP Open '%LPORT
        print '[+] '+str(reslt)
        n.close()
    except:
        print '[-]%d /TCP Close '%LPORT
def Portscan(LHOST,LPORT):
    try:
        IP=gethostbyname(LHOST)
    except:
        print "[-] Can not reverse '%s' unknow host"%LHOST
        return
    try:
       Name=gethostbyname(IP)
       print '\n[+]Scan result for '+Name[0]
    except:
        print '\n[+] Scan result for '+IP
    setdefaulttimeout(1)
    for port in LPORT:
        print 'Scan port '+port
        Connect(LHOST, int(port))
def main():
    name=optparse.OptionParser('usage%prog'+'-H [HOST] -P [PORT]')
    name.add_option('-H',dest='HOST',type='string',help='help me host')
    name.add_option('-P',dest='PORT',type='string',help='help me port')
    (options,args)=name.parse_args()
    HOST=options.HOST
    PORT=str(options.PORT).split(', ')
    if(HOST==None) | (PORT[0]==None):
        print '[-] Khong the thuc thi cac cong[s]'
        exit(0)
    Portscan(HOST, PORT)
if __name__ == '__main__':
    main()
