#! usr/bin/python 2.7
import sqlite3

def Main():
    try:
        c=sqlite3.connect('test1.db')

        cur=c.cursor()
        cur.execute('create table Student(ID INT,Name TEXT,Address TEXT)')
        cur.execute('insert into Student values(1,"Tom","VietNam")')
        cur.execute('insert into Student values(2,"Hary","American")')

        c.commit()

        cur.execute('select * from Student')
        data=cur.fetchall()

        for i in data:
            print i
    except sqlite3.Error:
        if c:
            print 'Error! Rolling back'
    else:
        if c:
            c.close()
if __name__ == '__main__':
    Main()