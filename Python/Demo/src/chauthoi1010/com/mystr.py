#!usr /bin/python
import __init__
import string
def main():
    str='  Le  Chau  Thoi  '
    str1=str[2:4]
    str2=str[6:11]
    str3=str[12:16]
    str4=str1+''+str2+''+str3
    print 'Name:',str4
if __name__ == '__main__':
    main()