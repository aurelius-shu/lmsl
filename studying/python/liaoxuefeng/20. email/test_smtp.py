from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 输入Email地址和口令:
from_addr = 'aurelius-shu@outlook.com'
# QQ 邮箱密码需换成短信授权码
password = input('password: ')
# 输入收件人地址:
to_addr = 'aurelius-shu@qq.com'
# 输入SMTP服务器地址:
smtp_server = 'smtp.office365.com'

# 邮件对象:
msg = MIMEMultipart('alternative')
msg['From'] = _format_addr('发件人 <%s>' % from_addr)
# 多个时以逗号分隔
msg['To'] = _format_addr('收件人 <%s>' % to_addr)
msg['Subject'] = Header('标题', 'utf-8').encode()

# msg = MIMEText(
#     '<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')
msg.attach(MIMEText('hello, send by Python...', 'plain', 'utf-8'))
# 邮件正文是MIMEText:
# msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
msg.attach(
    MIMEText(
        '<html><body><h1>Hello</h1><p><img src="cid:0"></p></body></html>',
        'html', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open(r'D:\Users\Aurelius\Pictures\threefish.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='threefish.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition',
                    'attachment',
                    filename='threefish.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 587)  # SMTP协议默认端口是25
# set_debuglevel(1) 可以打印 SMTP 服务器交互信息
server.set_debuglevel(1)
# 表示自己需要身份验证
server.ehlo()
# SMTP encryption method STARTTLS
server.starttls()
server.login(from_addr, password)
# [to_addr] 可以指定发送多人
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()