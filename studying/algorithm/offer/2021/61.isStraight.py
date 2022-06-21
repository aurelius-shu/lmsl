class Solution:
    def isStraight(self, nums):
        nums = sorted(nums)
        zores = []
        while nums[0] == 0:
            zores.append(0)
            nums = nums[1:]
        last = nums[0]
        for num in nums[1:]:
            while last + 1 != num and zores:
                if zores:
                    zores.pop()
                    last += 1
            if last + 1 != num:
                return False
            last = num
        if last == num:
            return True
        return False
