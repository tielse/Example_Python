#! usr/bin/python 2.7
import os
import cgi

print 'Content-type:text/html\r\n\r\n'
print '<html><head><title>Anonymous</title></head><body>'
print '<h1>Who Am I</h1>'
for i in range(5):
    print '<h3>Hello world'+str(i)+'</h3>'
print '</body></html>'