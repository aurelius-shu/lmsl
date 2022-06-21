import math

N = int(input())
nums = list(map(int, input().split(' ')))
res = 0
while N > 0:
    num = nums.pop()
    res = math.ceil((res + num) / 2)
    N -= 1
print(res)
