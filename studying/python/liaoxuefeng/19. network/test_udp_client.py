import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 不需要 connect()
    s.sendto(data, ('localhost', 6666))
    print(s.recv(1024).decode('utf-8'))
s.close()
