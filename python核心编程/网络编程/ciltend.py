import threading
import json
import tkinter
import tkinter.messagebox
import socket

IP = ''
PORT = ''
user = ''
listbox1 = ''
ii = 0
users = []
chat = '----------群聊----------'


root1 = tkinter.Tk()
root1.title('登录')
root1['height'] = 110
root1['width'] = 270
root1.resizable(0, 0)

IP1 = tkinter.StringVar()
IP1.set('127.0.0.1:50007')
User = tkinter.StringVar()
User.set('')

labelIP = tkinter.Label(root1, text='服务器地址')
labelIP.place(x=30, y=10, width=80, height=20)

entryIP = tkinter.Entry(root1, width=80, textvariable=IP1)
entryIP.place(x=120, y=10, width=130, height=20)

# 用户名标签
labelUser = tkinter.Label(root1, text='用户名')
labelUser.place(x=30, y=40, width=80, height=20)

entryUser = tkinter.Entry(root1, width=80, textvariable=User)
entryUser.place(x=120, y=40, width=130, height=20)

def login(*args):
    global IP, PORT, user
    IP, PORT = entryIP.get().split(':')
    PORT = int(PORT)
    user = entryUser.get()
    root1.destroy()

root1.bind('<Return>', login)

but = tkinter.Button(root1, text = '登入', command = login)
but.place(x = 100, y = 70, width = 70, height = 30)

root1.mainloop()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
if user:
    s.send(user.encode())
else:
    s.send('no'.encode())

addr = s.getsockname()
addr = addr[0]+':'+str(addr[1])
if user == '':
    user = addr


root = tkinter.Tk()
root.title(user)
root['height'] = 420
root['width'] = 580
root.resizable(0, 0)

#scorlly = tkinter.Listbox(root)
#scorlly.pack(side = tkinter.RIGHT,fill = tkinter.Y)

listbox = tkinter.Listbox(root)
listbox.place(x = 5, y = 0, width = 570, height = 365)

a = tkinter.StringVar()
a.set('')
entry = tkinter.Entry(root, width = 120, textvariable = a)
entry.place(x = 5, y = 375, width = 420, height = 30)


def send(*args):
    users.append('----------群聊----------')
    if chat not in users:
        tkinter.messagebox.showerror('发送失败', message='没有聊天对象!')
        return
    if chat == user:
        tkinter.messagebox.showerror('发送失败', message='不能私聊自己!')
        return
    mes = entry.get() + ':;' + user + ':;' + chat
    s.send(mes.encode())
    a.set('')

button = tkinter.Button(root, text='发送', command=send)
button.place(x=435, y=375, width=60, height=30)
root.bind('<Return>', send)

listbox1 = tkinter.Listbox(root)
listbox1.place(x = 445, y = 0, width = 130, height = 365)


def users():
    global listbox1, ii
    if ii == 1:
        listbox1.place(x=445, y=0, width=130, height=365)
        ii = 0
    else:
        listbox1.place_forget()
        ii = 1

def private(*args):
    global chat
    indexs = listbox1.curselection()
    index = indexs[0]
    chat = listbox1.get(index)
    if chat == '----------群聊----------':
        root.title(user)
        return
    ti = user + '  -->  ' + chat
    root.title(ti)


listbox1.bind('<ButtonRelease-1>', private)

def recv():
    global users
    while True:
        data = s.recv(1024)
        data = data.decode()
        try:
            data = json.loads(data)
            users = data
            listbox1.delete(0, tkinter.END)
            number = ('   在线人数：' + str(len(data)) + '人')
            listbox1.insert(tkinter.END, number)
            listbox1.itemconfig(tkinter.END, fg = 'green', bg = "#f0f0ff")
            listbox1.insert(tkinter.END,'----------群聊----------')
            listbox1.itemconfig(tkinter.END, fg = 'green')
            for i in range(len(data)):
                listbox1.insert(tkinter.END, (data[i]))
                listbox1.itemconfig(tkinter.END, fg = 'green')
        except:
            data = data.split(':;')
            data1 = data[0]
            data2 = data[1]
            data3 = data[2]
            if data3 == '----------群聊----------':
                listbox.insert(tkinter.END, data1)
                listbox.see(tkinter.END)
                u = data1.split(':')[0]
                if u == '' + user:
                    listbox.itemconfig(tkinter.END, fg = 'blue')
            elif data2 == user or data3 == user:
                listbox.insert(tkinter.END, data1)
                listbox.see(tkinter.END)
                listbox.itemconfig(tkinter.END, fg = 'red')

r = threading.Thread(target=recv)
r.start()

root.mainloop()
s.close()



