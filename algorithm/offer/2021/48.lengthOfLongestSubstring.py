class Solution:
    def __init__(self):
        self._d = {}
        self.first = 0
        self.last = -1
        self.maxlength = 1

    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        for i in range(len(s)):
            # 出现重复字符，且重复字符在滑动窗口区间内时，调整起始位置
            if s[i] in self._d and self._d[s[i]] >= self.first:
                self.first = self._d[s[i]] + 1
            self._d[s[i]] = i
            self.last += 1
            self.maxlength = max(self.maxlength, (self.last - self.first + 1))
        return self.maxlength


if __name__ == '__main__':
    s = Solution()
    res = s.lengthOfLongestSubstring("tmmzuxt")
    print(res)
