# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        first = self.BinarrySearch(data, k)
        last = self.BinarrySearch(data, k + 1)
        return last - first if first != len(data) and data[first] == k else 0

    def BinarrySearch(self, data, k):
        start, end = 0, len(data)
        while start < end:
            mid = (start + end) // 2
            if data[mid] >= k:
                end = mid
            else:
                start = mid + 1
        return start


if __name__ == '__main__':
    s = Solution()
    print(s.GetNumberOfK([1, 2, 3, 3, 3, 3], 3))
