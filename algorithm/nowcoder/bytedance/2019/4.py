N = int(input())
while N > 0:
    M = int(input())
    maxn = 1
    d, tmp = {}, {}
    while M > 0:
        nums = list(map(int, input().split(' ')))
        if nums[0] > 0:
            for i in range(nums[0]):
                key = '%s %s' % (nums[i * 2 + 1], nums[i * 2 + 2])
                tmp[key] = d.get(key, 0) + 1
                maxn = max(maxn, max(tmp.values()))
        d = tmp
        tmp = {}
        M -= 1
    print(maxn)
    N -= 1
