'''
Created on 2019年4月5日

@author: 17674
'''
from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

s = socket(AF_INET, SOCK_STREAM)
s.connect(ADDR)

info = ''
while info != '886':
    send_data = input("我:")
    mgs = s.recv(1024).decode()
    if send_data == '886':
        print("对方：" + mgs)
    s.send(send_data.encode())
s.close()
