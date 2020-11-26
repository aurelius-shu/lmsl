# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        nums = [str(num) for num in numbers]
        nums = self.quick_sort(nums)
        return ''.join(nums)

    def quick_sort(self, nums):
        if len(nums) < 2:
            return nums

        base = nums[0]
        less = [n for n in nums[1:] if self.compare(base, n)]
        greater = [n for n in nums[1:] if not self.compare(base, n)]
        return self.quick_sort(less) + [base] + self.quick_sort(greater)

    def compare(self, num1, num2):
        num12 = num1 + num2
        num21 = num2 + num1
        return num12 > num21


if __name__ == '__main__':
    s = Solution()
    r = s.PrintMinNumber([1, 11, 111])
    print(r)
