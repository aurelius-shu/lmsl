N,D=list(map(int, input().split(' ')))
nums=list(map(int, input().split(' ')))
res=0
left, right= 0, 2
while left < N-2:
    while right < N and nums[left]+D >= nums[right]:
        right +=1
    res+=((right-left-2)*(right-left-1))//2
    left+=1
print(res%99997867)