import socket
#创建udp套字节
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#参数ip和port的元组
s.bind(('127.0.0.1', 9999))
#接收请求
data, addr = s.recvfrom(1024)
#功能
data = float(data)*1.8+32
send_data = '温度：' + str(data)
print('来自于 %s:%s' % addr)

s.sendto(send_data.encode(), addr)
s.close()#关闭的是套接字，不是连接