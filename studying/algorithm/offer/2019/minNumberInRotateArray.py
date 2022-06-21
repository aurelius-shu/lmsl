# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        if len(rotateArray) <= 2:
            return min(rotateArray)
        mid_index = (len(rotateArray)) >> 1
        mid = rotateArray[mid_index]
        if mid >= rotateArray[0] and mid <= rotateArray[-1]:
            return self.minNumberInRotateArray(rotateArray[:mid_index])
        if mid <= rotateArray[0] and mid <= rotateArray[-1]:
            if rotateArray[mid_index] < rotateArray[mid_index - 1]:
                return rotateArray[mid_index]
            return self.minNumberInRotateArray(rotateArray[:mid_index])
        if mid >= rotateArray[0] and mid >= rotateArray[-1]:
            return self.minNumberInRotateArray(rotateArray[mid_index + 1:])


if __name__ == '__main__':
    l = [3, 4, 5, 1, 2]
    s = Solution()
    r = s.minNumberInRotateArray(l)
    print(r)
