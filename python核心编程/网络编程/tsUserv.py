'''
Created on 2019年4月5日

@author: 17674
'''
from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

updSerSock = socket(AF_INET, SOCK_STREAM)
updSerSock.bind(ADDR)

while True:
    print('waiting for connection ...')
    data, addr = updSerSock.recvfrom(BUFSIZ)
    updSerSock.sendto('[%s] %s' % (ctime() , data), addr)
    print('...received from and returned to:', addr)
updSerSock.close()