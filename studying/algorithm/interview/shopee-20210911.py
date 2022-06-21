class Solution:
    def threeSum(self, nums):

        if not nums:
            return []

        length = len(nums)

        if length < 3:
            return []

        result = set()

        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        l = [nums[i], nums[j], nums[k]]
                        list.sort(l)
                        result.add('|'.join([str(i) for i in l]))

        result = [[int(i) for i in row.split('|')] for row in result]
        return result


if __name__ == '__main__':
    input = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    result = s.threeSum(input)
    print(result)
