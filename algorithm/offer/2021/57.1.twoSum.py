class Solution:
    def twoSum(self, nums, target):
        first, last = 0, len(nums) - 1
        while first < last and nums[first] + nums[last] != target:
            if nums[first] + nums[last] > target:
                last -= 1
            else:
                first += 1
        if first < last:
            return nums[first], nums[last]
        else:
            return None
