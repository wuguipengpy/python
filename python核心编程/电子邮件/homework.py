import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header


#构建邮件
from_addr = '985821966@qq.com'
from_password = 'aymlgvxjqjgwbcgj'
to_addr = ['17674101779@163.com', '985821966@qq.com']#列表可以进行邮件群发

#构建邮件

msg = MIMEMultipart('mixed')#内容
msg['from'] = Header('吴桂鹏', 'utf-8')#发件人
msg['to'] = Header('康老师', 'utf-8')#收件人
sub = '一次作业'
msg['subject'] = Header(sub, 'utf-8')#主题

#超链接
html = """
<p>184962020017 吴桂鹏</p>
<p><a href = "http://www.baidu.com">点击进入百度</a><br>"""
text_html = MIMEText(html,'html', 'utf-8')
msg.attach(text_html)


#添加附件
sendfile=open('qqq.txt','rb').read()
text_att = MIMEText(sendfile, 'base64', 'utf-8')
text_att["Content-Type"] = 'application/octet-stream'
#以下附件可以重命名成aaa.txt
#text_att["Content-Disposition"] = 'attachment; filename="aaa.txt"'
#另一种实现方式
text_att.add_header('Content-Disposition', 'attachment', filename='qqq.txt')
#以下中文测试不ok
#text_att["Content-Disposition"] = u'attachment; filename="中文附件.txt"'.decode('utf-8')
msg.attach(text_att)

#发送邮件
try:
    svr = smtplib.SMTP('smtp.qq.com', 25)#连接服务器
    svr.login(from_addr, from_password)#登录
    svr.sendmail(from_addr, to_addr, msg.as_string())
    svr.quit()
    print('发送成功')
except Exception as e:
    print(e)

