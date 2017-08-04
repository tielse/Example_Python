import optparse
from socket import *
from threading import *
Lock=Semaphore(value=1)
def connScan(Host,Port):
	try:
		connSkt=socket(AF_INET,SOCK_STREAM)
		connSkt=connect((Host,Port))
		connSkt.send('ViolentPython\r\n')
		res=connSkt.recv(100)
		Lock.acquire()
		print '[+]%d/tcp open '% Port
		print '[+] '+str(res)
	except:
		Lock.acquire()
		print '[-]%d/tcp closed '% Port
	finally:
		Lock.acquire()
		connSkt.close()
def portScan(Host,Ports):
	try:
		tgIP=gethostbyname(Host)
	except:
		print "[-] Cannot resolve '%s': Unknown host"%tgIP
		return
	try:
		tgName=gethostbyname(tgIP)
		print '\n[+] Scan Results for: '+tgName[0]
	except:
		print '\n[+] Scan Results for:' +tgIP
	setdefaulttimeout(1)
	for Port in Ports:
		t=Thread(target=connScan,args=(Host,int(Port)))
		t.start()
def main():
	parser = optparse.OptionParser('usage%prog ' +\
  		'-H <target host> -p <target port>')
	parser.add_option('-H', dest ='Host', type ='string', \
 		help ='specify target host')
	parser.add_option('-p', dest ='Port', type ='string', \
 		help ='specify target port[s] separated by comma')
	(options,args)=parser.parse_args()
	Host=options.Host
	Ports=str(options.Port).split(', ')
	if(Host==None) | (Ports[0] == None):
		print parser.usage
		exit(0)
	portScan(Host, Ports)
if __name__ == '__main__':
	main()