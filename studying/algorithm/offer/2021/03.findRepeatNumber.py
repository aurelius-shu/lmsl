class Solution:
    def __init__(self):
        self._d = {}

    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in nums:
            if i in self._d:
                return i
            self._d[i] = 1
        return None
