from io import StringIO, BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read().decode('utf-8'))

f = StringIO()
f.write('hello')
# 读取写入的 str
print(f.getvalue())

f = StringIO('hello, 中国')
print(f.read())