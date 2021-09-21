class Solution:
    def findContinuousSequence(self, target):
        res = []
        first, last = target // 2, target // 2 + 1

        # 两个终止条件：
        #   1. first < 1
        #   2. first = 1 and sum(nums) < target
        while first >= 1 and not (first == 1 and (first + last) / 2 * (last - first + 1) < target):
            s = (first + last) / 2 * (last - first + 1)
            if s <= target:
                if s == target:
                    res.append(list(range(first, last + 1)))
                first -= 1
            else:
                last -= 1
        return res[::-1]


if __name__ == '__main__':
    s = Solution()
    res = s.findContinuousSequence(15)
    print(res)
