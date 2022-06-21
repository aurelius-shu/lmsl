class Solution:
    def exchange(self, nums):
        if not nums:
            return nums

        head, tail = 0, len(nums) - 1
        while head < tail:
            while head < tail and nums[head] & 1 == 1:
                head += 1
            while head < tail and nums[tail] & 1 == 0:
                tail -= 1
            nums[head], nums[tail] = nums[tail], nums[head]
        return nums


if __name__ == '__main__':
    s = Solution()
    res = s.exchange([1, 3, 5])
    print(res)
