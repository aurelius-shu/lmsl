class Solution:
    def __init__(self):
        self.nums = []
        self.target = None

    def search(self, nums, target):
        if not nums:
            return 0
        self.nums = nums
        self.target = target
        count = 0
        index = self.find(0, len(nums) - 1)
        if index is None:
            return count
        count += 1
        left, right = index, index
        while right + 1 < len(nums) and nums[right + 1] == target:
            right += 1
            count += 1
        while left - 1 > -1 and nums[left - 1] == target:
            left -= 1
            count += 1
        return count

    def find(self, first, last):
        if first > last:
            return None
        if first == last and self.nums[first] != self.target:
            return None
        mid = first + ((last - first) >> 1)
        if self.nums[mid] == self.target:
            return mid
        left = self.find(first, mid)
        right = self.find(mid + 1, last)
        return left if left is not None else right
