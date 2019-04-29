import socket
import threading
import queue
import json

IP = '127.0.0.1'
PORT = 50007

que = queue.Queue()
users = []
lock = threading.Lock()

def tcp_connect(conn, addr):
    user = conn.recv(1024)
    user = user.decode()
    if user == 'no':
        user = addr[0]+'.'+str(addr[1])
    users.append((conn, user, addr))
    print('新连接:',addr,end = '')
    d = onlines()
    recv(addr,d)
    try:
        while True:
            data = conn.recv(1024)
            data = data.decode()
            recv(addr, data)
        conn.close()
    except:
        print(user+'断开连接')
        delUsers(conn, addr)
        conn.close()

def delUsers(conn, addr):
    a = 0
    for i in users:
        if i[0] == conn:
            users.pop(a)
            print('剩余在线用户:', end = '')
            d = onlines()
            recv(addr, d)
            print(d)
            break
        a += 1


def recv(addr, data):
    lock.acquire()
    try:
        que.put((addr, data))
    finally:
        lock.release()

def sendData():
    while True:
        if not que.empty():
            data = ''
            message = que.get()
            if isinstance(message[1],str):
                for i in range(len(users)):
                    for j in range(len(users)):
                        if message[0] == users[j][2]:
                            data = '' + users[j][1] + ':' +message[1]
                            break
                    users[i][0].send(data.encode())
                data = data.split(':;')[0]
                print(data)
                if isinstance(message[1],list):
                    data = json.dumps(message[1])
                    for i in range(len(users)):
                        users[i][0].send(data.encode())




def onlines():
    online =[]
    for i in range(len(users)):
        online.append(users[i][1])
    return online

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(5)
print('等待连接')
q = threading.Thread(target=sendData)
q.start()
while True:
    conn, addr = s.accept()
    t = threading.Thread(target=tcp_connect, args=(conn, addr))
s.close()

