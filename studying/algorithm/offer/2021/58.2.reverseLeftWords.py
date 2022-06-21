class Solution:
    def reverseLeftWords(self, s, n):
        return s[n:] + s[:n]
