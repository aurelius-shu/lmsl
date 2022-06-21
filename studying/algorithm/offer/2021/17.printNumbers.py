class Solution:
    def printNumbers(self, n):
        return list(range(1, 10 ** n))


if __name__ == '__main__':
    s = Solution()
    print(s.printNumbers(5))
