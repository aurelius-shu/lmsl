class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._data = []
        self._min = []

    def push(self, x: int) -> None:
        self._data.append(x)
        if not self._min:
            self._min.append(x)
        else:
            m = min(self._min[-1], x)
            self._min.append(m)

    def pop(self) -> None:
        self._min.pop()
        return self._data.pop()

    def top(self) -> int:
        return self._data[-1]

    def min(self) -> int:
        return self._min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
