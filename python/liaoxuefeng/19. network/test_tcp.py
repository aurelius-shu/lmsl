import socket

# AF_INET指定使用IPv4协议
# SOCK_STREAM指定使用面向流的TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# HTTP 协议规定客户端必须先请求，再由服务端接收后发数据给客户端
s.connect(('www.sina.com.cn', 80))

buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

s.close()

# 分割一次
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

with open('sina.html', 'wb') as f:
    f.write(html)