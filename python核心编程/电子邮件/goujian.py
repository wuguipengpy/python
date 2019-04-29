from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.header import Header

#设置用户密码收件人
send = '985821966@qq.com'
password = 'aymlgvxjqjgwbcgj'
recv = ['17674101779@163.com', '985821966@qq.com']

#mixed--混合型元素
#alternative --文本混合
#relates--多媒体元素

msgRoot = MIMEMultipart('mixed')#内容
msgRoot['from'] = Header('我', 'utf-8')#发件人
msgRoot['to'] = Header('你', 'utf-8')#收件人
sub = '一次事件'
msgRoot['subject'] = Header(sub, 'utf-8')#主题

#普通文本
text_text = '这就是个测试的普通文本'

msg_text = MIMEText(text_text, 'plain', 'utf-8')

#超文本
mail_msg = """
<p>Python 邮件发送网页...</p>
<p><a href="http://www.baidu.com">百度</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""
msg_html=MIMEText(mail_msg, 'html', 'utf-8')

#指定图片构造
with open('text.png','rb') as file:
    msg_Image = MIMEImage(file.read())
    msg_Image.add_header('Content-ID', '<image1>')


#指定附件构造
with open('python邮件构建代码.txt', 'rb')  as sendfile:
    msg_att = MIMEText(sendfile.read(), 'base64', 'utf-8')#实例
    msg_att['Content-Type'] = 'application/octet-stream'
    msg_att.add_header('Content-Disposition', 'attachment', filename = 'python邮件构建代码.txt')

msgRoot.attach(msg_text)
msgRoot.attach(msg_html)
msgRoot.attach(msg_att)
msgRoot.attach(msg_Image)

try:
    import smtplib
    svr = smtplib.SMTP('smtp.qq.com', 25)#连接服务器
    svr.login(send, password)#登录
    svr.sendmail(send, recv, msgRoot.as_string())
    svr.quit()
    print('发送成功')
except:
    print('出错')