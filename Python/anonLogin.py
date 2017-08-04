import ftplib
def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymous', 'chauthoi1010@gmail.com')
		print '\n[*] ' + str(hostname) +\
			' FTP Anonymous Logon Succeeded.'
		ftp.quit()
		return True
	except Exception, e:
		print '\n[-] ' + str(hostname) +\
			' FTP Anonymous Logon Failed.'
		return False
host = '192.168.1.108'
anonLogin(host)