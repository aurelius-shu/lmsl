class Solution:
    def __init__(self):
        self.order = None

    def verifyPostorder(self, postorder):
        if len(postorder) < 3:
            return True

        self.order = postorder
        return self.verify(0, len(postorder) - 1)

    def verify(self, start, end):

        if end - start < 3:
            return True

        left_start, right_end = start, end - 1
        mid = right_end
        while mid >= start and self.order[mid] > self.order[end]:
            mid -= 1
        while mid >= start:
            if self.order[mid] > self.order[end]:
                return False
            mid -= 1
        left_end, right_start = mid, mid + 1
        return self.verify(left_start, left_end) and self.verify(right_start, right_end)


if __name__ == '__main__':
    s = Solution()
    res = s.verifyPostorder([1, 2, 5, 10, 6, 9, 4, 3])
    print(res)
