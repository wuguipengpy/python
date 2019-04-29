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

s = socket(AF_INET, SOCK_STREAM)
s.bind(ADDR)#绑定ip
s.listen(5)#监听
sock, addr = s.accept()
print('已连接')


#功能
info = sock.recv(1024).decode()
while info != '886':
    if info:
        print('对方:' +info)
    send_data = input("我:")
    sock.send(send_data.encode())
    if send_data=='886':
        break
    info = sock.recv(1024).decode()
s.close()
sock.close()