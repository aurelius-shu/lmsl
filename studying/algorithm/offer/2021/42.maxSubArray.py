class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0
        cursum, maxsum = nums[0], nums[0]
        for num in nums[1:]:
            pre = cursum
            cursum = num if cursum < 0 else cursum + num
            maxsum = max(pre, cursum, maxsum)
        return maxsum
