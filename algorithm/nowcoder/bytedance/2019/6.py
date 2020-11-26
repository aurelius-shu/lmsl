def funx(a, b):
    return (a // b, a % b)


res = 0
a = 1024 - int(input())
n, a = funx(a, 64)
res += n
n, a = funx(a, 16)
res += n
n, a = funx(a, 4)
res += n + a
print(res)
