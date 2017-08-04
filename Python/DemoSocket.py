import socket
def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
 		return banner
	except:
 		return
def main():
	ip1 = '192.168.95.148'
	ip2 = '192.168.95.149'
	port = 21
	banner1 = retBanner(ip1, port)
	if banner1:
		print '[+] ' + ip1 + ': ' + banner1
		banner2 = retBanner(ip2, port)
	if banner2:
		print '[+] ' + ip2 + ': ' + banner2
if __name__ == '__main__':
	main()