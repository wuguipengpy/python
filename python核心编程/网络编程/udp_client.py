import socket
#创建udp套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = input("请输入:")
try:
    s.sendto(data.encode(), ('127.0.0.1', 9999))#encode编码
    print(s.recv(1024).decode())#decode解码
except:
    s.close()