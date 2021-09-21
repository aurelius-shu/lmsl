class Solution:
    def missingNumber(self, nums):
        if not nums:
            return 0
        index = self.find(0, len(nums) - 1, nums)
        return index if index is not None else len(nums)

    def find(self, first, last, nums):
        if first > last:
            return None
        if first == last and nums[first] != first:
            return first
        mid = first + (last - first) // 2
        if nums[mid] == mid:
            first = mid + 1
        else:
            last = mid
        left = self.find(first, mid, nums)
        right = self.find(mid + 1, last, nums)
        return left if left is not None else right
