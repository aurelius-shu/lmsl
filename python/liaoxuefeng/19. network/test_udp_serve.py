import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# UDP 不需要listen()，直接接收
s.bind(('localhost', 6666))

print('bind udp on 6666...')

while True:
    # 返回数据和客户端IP、端口
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    # 向客户端回发
    s.sendto(b'Hello, %s.' % data, addr)
