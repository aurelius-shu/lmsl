# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        dp = [1] * (number + 1)
        for i in range(2, number + 1):
            for j in range(1, i + 1):
                dp[i] = max(dp[i], max(j * (i - j), dp[j] * (i - j)))
        return dp[number]
