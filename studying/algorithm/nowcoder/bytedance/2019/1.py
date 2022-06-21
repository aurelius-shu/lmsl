N=int(input())
while N>0:
    res=[]
    s=input()
    for e in s:
        if len(res) < 2:
            res.append(e)
            continue
        if len(res)>=2 and res[-1]==e and res[-1]==res[-2]:
            continue
        if len(res)>=3 and res[-1]==e and res[-3]==res[-2]:
            continue
        res.append(e)
    N-=1
    print(''.join(res))
