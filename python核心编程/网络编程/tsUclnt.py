'''
Created on 2019年4月5日

@author: 17674
'''
from socket import *
from click._compat import raw_input

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

updCliSock = socket(AF_INET, SOCK_DGRAM)


while True:
    data = input('>')
    if not data:
        break
    updCliSock.send(data, ADDR)
    data, ADDR = updCliSock.recvFROM(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))
    
updCliSock.close()