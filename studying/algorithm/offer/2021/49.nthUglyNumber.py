class Solution:
    def __init__(self):
        self.p2 = 1
        self.p3 = 1
        self.p5 = 1
        self.dp = {1: 1}

    def nthUglyNumber(self, n):
        for i in range(1, n):
            next = min(self.dp[self.p2] * 2, self.dp[self.p3] * 3, self.dp[self.p5] * 5)
            while next == self.dp[i]:
                if next == self.dp[self.p2] * 2:
                    self.p2 += 1
                elif next == self.dp[self.p3] * 3:
                    self.p3 += 1
                else:
                    self.p5 += 1
                next = min(self.dp[self.p2] * 2, self.dp[self.p3] * 3, self.dp[self.p5] * 5)
            self.dp[i + 1] = next
        return self.dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.nthUglyNumber(10))
