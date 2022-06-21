def consumer():
    r = ''
    while True:
        # 2. 通过 yield 回传 r 给 send 调用
        # 4. 接收 send 的消息 n
        n = yield r
        if not n:
            return
        print(f'[CONSUMER] Consuming {n}...')
        r = '200 OK'


def produce(c):
    # 1. 启动生成器
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print(f'[PRODUCER] Producing {n}...')
        # 3. 发送消息 n 返回给 yield
        # 5. 接收 yield 的结果 r
        r = c.send(n)
        print(f'[PRODUCER] Consumer return: {r}')
    # 6. 关闭生成器
    c.close()


# 消费者 - 生成器对象
c = consumer()
produce(c)