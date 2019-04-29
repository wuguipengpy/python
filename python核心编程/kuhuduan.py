import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接

s.connect(("www.hnkjxy.net.cn", 80))

s.send(b'GET/ HTTP / 1.1\r\n HOST:www.hnkjxy.net.cn \r\n Connection:clase \r\n\r\n')

# 接收数据

data = []
while True:
    d = s.recv(1024)  # 按字节接收数据
    if d:
        data.append(d)  # 将接受的数据加入列表
    else:
        break

datab = b''.join(data)  # 转换成二进制数据
s.close()
print(datab)

header, html = datab.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

with open('wodewangzhi.html', 'wb') as file:
    file.write(html)