#-*- coding:utf-8 -*-
"""
题目：
    30. 包含min函数的栈
    定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

    示例:

    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.min();   --> 返回 -3.
    minStack.pop();
    minStack.top();      --> 返回 0.
    minStack.min();   --> 返回 -2.
     

    提示：

    各函数的调用总次数不超过 20000 次

思路：
    依据：随着入栈，栈的最小值越来越小
    使用一个辅助栈，记录每次入栈时刻的最小值
    对应的出栈时，弹出辅助栈顶一个值，辅助栈顶即可始终记录当前栈中的最小值
"""


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.mins = []

    def push(self, x: int) -> None:
        self.data.append(x)
        self.mins.append(
            x if not self.mins or x < self.mins[-1] else self.mins[-1])

    def pop(self) -> None:
        self.data.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.data[-1]

    def min(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()