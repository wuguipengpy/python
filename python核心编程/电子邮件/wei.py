from email.mime.text import MIMEText#调用构建邮件文本
from email.header import Header#调用头文件
import smtplib
from email.mime.multipart import MIMEMultipart#调用多个方式文件

#构建邮件
from_addr = '985821966@qq.com'
from_password = 'aymlgvxjqjgwbcgj'
to_addr = ['17674101779@163.com', '985821966@qq.com']#列表可以进行邮件群发

#构建邮件
thmltext = '''
<p>python 测试</p>
<p><a href = "https://ilovefishc.com/html5/html5/lesson0/love/index.html">点击一下， 钱就没了</a><br>'''

msg = MIMEMultipart(thmltext, 'html', 'utf-8')#内容
msg['from'] = Header('我', 'utf-8')#发件人
msg['to'] = Header('你', 'utf-8')#收件人
sub = '一次事件'
msg['subject'] = Header(sub, 'utf-8')#主题

#添加附件
with open('qqq.txt', 'rb') as file:
    s = file.read()
    m = MIMEText(s, 'base64', 'utf_8')
    m['Content-Type'] = 'application/octet-stream'
    m['Content-Disposition'] = 'attachment;filename = "qqq.txt"'
    #添加到msg
    msg.attach(m)

#发送邮件

svr = smtplib.SMTP('smtp.qq.com', 25)#连接服务器
svr.login(from_addr, from_password)#登录
svr.sendmail(from_addr, to_addr, msg.as_string())
print('发送成功')



