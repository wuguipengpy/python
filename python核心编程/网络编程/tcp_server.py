import socket

# 创建服务端的socket对象socketserver
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9092
# 绑定地址（包括ip地址会端口号）
s.bind((host, port))
# 设置监听
s.listen(5)
# 等待客户端的连接
# 注意：accept()函数会返回一个元组
# 元素1为客户端的socket对象，元素2为客户端的地址(ip地址，端口号)
sock, addr = s.accept()

# while循环是为了能让对话一直进行，直到客户端输入q
while True:

    # 接收客户端的请求
    recvmsg = sock.recv(1024)
    # 把接收到的数据进行解码
    strData = recvmsg.decode("utf-8")
    # 判断客户端是否发送q，是就退出此次对话
    if strData == 'q':
        break
    print("对方:" + strData)
    msg = input("我:")
    # 对要发送的数据进行编码
    sock.send(msg.encode("utf-8"))

s.close()