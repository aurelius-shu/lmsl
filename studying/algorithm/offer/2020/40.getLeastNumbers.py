#-*- coding:utf-8 -*-
"""
题目：
    40. 最小的k个数
    输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

    示例 1：
    输入：arr = [3,2,1], k = 2
    输出：[1,2] 或者 [2,1]

    示例 2：
    输入：arr = [0,1,2,1], k = 1
    输出：[0]

    限制：
    0 <= k <= arr.length <= 10000
    0 <= arr[i] <= 10000

    思路：
    堆排序，快速排序等
    要求最小值，则挤出最大值的办法
    当当前值比堆中最大的要小，则弹出最大值，将当前值压入堆中

    注意：
    Python 对是小根堆，存储值需要取反以便从堆顶拿到当前排序的最大值
"""

import heapq


class Solution:
    def getLeastNumbers(self, arr, k):
        res = []
        if k == 0:
            return res

        head, tail = arr[:k], arr[k:]
        for i in head:
            heapq.heappush(res, -i)

        for i in tail:
            if -res[0] > i:
                heapq.heappop(res)
                heapq.heappush(res, -i)
        return [-i for i in res]


if __name__ == "__main__":
    l = [5, 4, 1, 3, 2, 4]
    # s = Solution()
    # res = s.getLeastNumbers(l, 3)
    # print(res)
    res = []
    for i in l:
        heapq.heappush(res, i)
    print(res)
    for i in range(len(res)):
        print(heapq.heappop(res))
        print(res)
