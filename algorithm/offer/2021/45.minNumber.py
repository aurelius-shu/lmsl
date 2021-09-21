class Solution:
    def minNumber(self, nums):
        if not nums:
            return ""

        length = len(nums)
        for i in range(length):
            for j in range(length - i - 1):
                if self.compare(nums[j], nums[j + 1]):
                    nums[j + 1], nums[j] = nums[j], nums[j + 1]
        return ''.join([str(num) for num in nums])

    def compare(self, a, b):
        ab = str(a) + str(b)
        ba = str(b) + str(a)
        return int(ab) > int(ba)
