

def application(environ, start_application):
    start_application('200 OK', [('Content-Type', 'text/html')])
    body = "<h1>Hello %s!</H1>" % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf8')]


from wsgiref.simple_server import make_server
# from wsgiprog import application
httpd = make_server('localhost', 9997, application)
httpd.serve_forever()
