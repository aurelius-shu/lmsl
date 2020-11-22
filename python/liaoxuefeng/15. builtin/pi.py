import itertools


def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    natuals = itertools.count(1)
    odd = filter(lambda x: x % 2 > 0, natuals)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    odd = itertools.takewhile(lambda x: (x + 1) // 2 <= N, odd)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    items = map(lambda x: (4 / (x if (((x + 1) // 2) % 2 > 0) else (0 - x))),
                odd)
    # step 4: 求和:
    return sum(items)


if __name__ == "__main__":
    print(pi(10000))