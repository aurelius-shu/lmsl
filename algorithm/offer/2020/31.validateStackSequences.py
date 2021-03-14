#-*- coding:utf-8 -*-
"""
题目：
    31. 栈的压入、弹出序列
    输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

    示例 1：

    输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
    输出：true
    解释：我们可以按以下顺序执行：
    push(1), push(2), push(3), push(4), pop() -> 4,
    push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
    示例 2：

    输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
    输出：false
    解释：1 不能在 2 之前弹出。
     
    提示：

    0 <= pushed.length == popped.length <= 1000
    0 <= pushed[i], popped[i] < 1000
    pushed 是 popped 的排列。

思路：
    使用一个辅助栈模拟入栈和出栈过程，如果最终全部弹出成功，则popped是该压入栈序列的弹出序列

    先决条件：入序或出序不为空
    出栈：stack 和 出序不为空 且 stack[-1] == popped[0]
    入栈：pushed 不为空
    else：break
"""


class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stack = []
        while pushed or popped:
            if stack and popped and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
            elif pushed:
                stack.append(pushed.pop(0))
            else:
                break

        return not stack and not popped