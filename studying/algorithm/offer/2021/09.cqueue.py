class CQueue:

    def __init__(self):
        self._input = []
        self._output = []

    def appendTail(self, value: int) -> None:
        self._input.append(value)

    def deleteHead(self) -> int:
        if not self._output:
            while self._input:
                self._output.append(self._input.pop())
        if self._output:
            return self._output.pop()
        return -1

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
