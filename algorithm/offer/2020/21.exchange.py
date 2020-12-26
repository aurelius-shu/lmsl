#-*- coding:utf-8 -*-
"""
题目：
    21. 调整数组顺序使奇数位于偶数前面
    输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

思路：
双指针，一头一尾
头部遇奇后移，尾部遇偶前移，指针相遇时结束
当两个指针同时停下时，交换，继续移动

注意：
"""


class Solution:
    def exchange(self, nums):
        head, tail = 0, len(nums) - 1

        while head < tail:
            if nums[head] & 1 == 0 and nums[tail] & 1 == 1:
                nums[head], nums[tail] = nums[tail], nums[head]
            if nums[head] & 1 == 1:
                head += 1
            if nums[tail] & 1 == 0:
                tail -= 1
        return nums


s = Solution()
res = s.exchange([1, 2, 3, 4])
print(res)
