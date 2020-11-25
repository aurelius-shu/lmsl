import asyncio


# @aysncio.coroutine 把 generator 标记成 coroutine
# @asyncio.coroutine
async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    # yield from 调用 connect 生成器，并接受 connect 的调用结果
    # 主线程并未等待 connect 调用，而是执行 EventLoop 中其他 coroutine
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()
tasks = [
    wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']
]
# 把 coroutine 扔到 EventLoop 中执行
loop.run_until_complete(asyncio.wait(tasks))
loop.close()