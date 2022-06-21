class Solution:
    def majorityElement(self, nums):
        if not nums:
            return None

        char = nums[0]
        count = 1
        for num in nums[1:]:
            if num == char:
                count += 1
            else:
                if count < 1:
                    count = 1
                    char = num
                else:
                    count -= 1
        return char
