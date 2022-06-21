class Solution:
    def singleNumber(self, nums):
        bins = [bin(num)[2:] for num in nums]
        grid = [0] * max([len(b) for b in bins])

        for b in bins:
            for i, n in enumerate(b[::-1]):
                grid[i] += int(n)
        grid = grid[::-1]
        for i in range(len(grid)):
            grid[i] %= 3
        binres = ''.join([str(d) for d in grid])
        return int(binres, base=2)


if __name__ == '__main__':
    nums = [86, 38, 67, 65, 61, 72, 42, 1, 17, 88, 65, 72, 64, 54, 22, 45, 92, 1, 38, 17, 3, 68, 34, 64, 29, 27, 6, 22,
            54, 56, 34, 61, 38, 92, 48, 82, 73, 62, 86, 27, 11, 6, 22, 98, 86, 37, 15, 61, 88, 29, 73, 15, 62, 1, 6, 67,
            11, 72, 16, 87, 67, 62, 42, 16, 45, 98, 7, 27, 87, 37, 16, 56, 88, 64, 15, 68, 42, 98, 29, 82, 65, 82, 54,
            7, 17, 68, 92, 45, 37, 87, 56, 11, 48, 34, 7, 48, 73]
    # nums = [3, 4, 3, 3]
    s = Solution()
    res = s.singleNumber(nums)
    print(res)
