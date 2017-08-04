#! usr/bin/python 2.7
import os
import cgi

print 'Content-type:text/html\r\n\r\n'
print '<html><head><title>Anonymous</title></head><body>'
print '<h1>Who Am I</h1>'
form = cgi.FieldStorage()
if form.getvalue('name'):
    name=form.getvalue('name')
    print '<h3>Hello '+name+'! Thanks for using my script!</h3></br>'
if form.getvalue('happy'):
    print "<p>Yes! I'm happy too!"
if form.getvalue('sad'):
    print "Yes! I'm very sad!"

print "<form method='post' action='myCGI2.py'>"
print "<p>Name:<input type='text' name='name' /></p>"
print "<input type='checkbox' name='name' />Happy"
print "<input type='checkbox' name='name' />"
print "<input type='submit' value='Submit' />"
print '</form>'
print '</body></html>'