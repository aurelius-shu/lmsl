def application(environ, start_response):
    start_response('200 oK', [('Content-Type', 'text/html')])
    body = f"<h1>Hello, {environ['PATH_INFO'][1:] or 'web'}!</h1>"
    return [body.encode('utf-8')]


from wsgiref.simple_server import make_server

# 创建一个服务器，IP地址为空，端口是 8000，处理函数是 application
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP 请求
httpd.serve_forever()