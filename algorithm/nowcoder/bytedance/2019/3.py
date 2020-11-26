def isHu(nums):
    if not nums:
        return True
    n = len(nums)
    count0 = nums.count(nums[0])
    if n % 3 != 0 and count0 >= 2 and isHu(nums[2:]):
        return True
    if count0 >= 3 and isHu(nums[3:]):
        return True
    if nums[0] + 1 in nums and nums[0] + 2 in nums:
        copy_nums = nums.copy()
        copy_nums.remove(nums[0])
        copy_nums.remove(nums[0] + 1)
        copy_nums.remove(nums[0] + 2)
        return isHu(copy_nums)
    return False


def main(nums):
    res, d = [], {}
    for num in nums:
        d[num] = d.get(num, 0) + 1
    select_list = set(range(1, 10)) - set(key for key, val in d.items() if val == 4)
    for select in select_list:
        if isHu(sorted(nums + [select, ])):
            res.append(str(select))
    print(' '.join(res) if len(res) > 0 else '0')


nums = list(map(int, input().split(' ')))
main(nums)
