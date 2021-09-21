from functools import reduce


class Solution:
    def singleNumbers(self, nums):
        xor = reduce(lambda x, y: x ^ y, nums)
        dif = 1
        while dif & xor == 0:
            dif <<= 1

        a, b = 0, 0
        for num in nums:
            if dif & num:
                a ^= num
            else:
                b ^= num
        return [a, b]
