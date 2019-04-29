import poplib  # 导入方法
from email.header import decode_header  # head文件解码模块
from email.parser import Parser  # 邮件解码模块
from email.utils import parseaddr

svr = poplib.POP3_SSL('pop.qq.com')
sender = '985821966@qq.com'
password = 'aymlgvxjqjgwbcgj'

svr.user(sender)#输入邮箱
svr.pass_(password)#输入验证码
#stat方法放回一个元组， 为邮件数量和占用空间
msgs, counts = svr.stat()
print('message:{0}, size:{1}'.format(msgs, counts))
#返回所有邮件的编号列表
rsp1, mails1, cotect1 = svr.list()
print(mails1)

#获取信件
rsp, lines, octets = svr.retr(len(mails1))

#获得邮件的整个原始文本

msgs_count = b'\r\n'.join(lines).decode('utf-8')

#解析邮件
msgs = Parser().parsestr(msgs_count)#解码邮件整体

#srt解码
def decodeStr(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


#判断邮件编码
def guessCharset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()#找到内容，转换为空
        pos = content_type.find('charset = ')
        if pos >= 0:
            charset = content_type[pos+8:].setip()#如果charset包含， 则内容为
    return charset


#定义邮件解码主程序
def parseMsg(msg, indent = 0):
#提取头部信息， 内容只有一个
    if indent ==0:
        for header in['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_header(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decodeStr(hdr)
                    value = '{0}, <{1}>'.format(name, addr)
            print('{0}, <{1}>'.format(indent, header, value))


#提取邮件元素
    if(msg.is_multipart()):
        #如果邮件为multopart类型， 则调用递归解析
        #分包
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('{0}sparts:{1}'.format('', indent, n))
            parseMsg(part, indent+1)
    else:#最基本的邮件
        content_type = msg.get_content_type()
        if content_type == "text/plain" or content_type == 'text/html':
            content_type = msg.get_payload(decode=True)
            charset = guessCharset(msg)
            if charset:
                content = content.decode(charset)
            print('{0}Text:{1}'.format(indent, content_type))
        else:
            print('{0}Attachment:{1}'.format(indent, content_type))


parseMsg(msgs, 0)