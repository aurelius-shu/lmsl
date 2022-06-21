# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        start, end, csum = 0, len(array) - 1, array[0] + array[len(array) - 1]
        while start < end:
            if csum < tsum:
                csum -= array[start]
                start += 1
                csum += array[start]
            elif csum > tsum:
                csum -= array[end]
                end -= 1
                csum += array[end]
            else:
                return [array[start], array[end]]
        return []


if __name__ == '__main__':
    s = Solution()
    print(s.FindNumbersWithSum([], 0))
