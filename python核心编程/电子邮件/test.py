from email.mime.text import MIMEText#调用构建邮件文本

while True:
#构建电子邮件内容
    msg_text = MIMEText('你怎么那么像蔡徐坤', 'plain')

    import smtplib
    svr = smtplib.SMTP('smtp.qq.com', 25)#连接服务器
    svr.login('985821966@qq.com', 'aymlgvxjqjgwbcgj')#登录
    svr.sendmail('985821966@qq.com', '2019266303@qq.com', msg_text.as_string())
    print('发送成功')
