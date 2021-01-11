#-*- coding:utf-8 -*-
"""
题目：
    35. 复杂链表的复制
    请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

    示例 1：

    输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
    示例 2：

    输入：head = [[1,1],[2,1]]
    输出：[[1,1],[2,1]]
    示例 3：

    输入：head = [[3,null],[3,0],[3,null]]
    输出：[[3,null],[3,0],[3,null]]
    示例 4：

    输入：head = []
    输出：[]
    解释：给定的链表为空（空指针），因此返回 null。
     
    提示：

    -10000 <= Node.val <= 10000
    Node.random 为空（null）或指向链表中的节点。
    节点数目不超过 1000 。


思路：
1. 遍历链表，复制一个节点插入到当前节点的后面
2. 将偶数位节点的随机指针指向当前所知节点的下一个（null不动）
3. 将所有节点的 next 指针指向当前节点的下一个

注意：
第一步添加复制节点后，节点要后移两位
第三步移动next指针时，使用双指针更方便，判断停止条件使用后一个指针指向为None
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        node = head
        while node:
            copy = Node(node.val, node.next, node.random)
            copy.next = node.next
            node.next = copy
            node = node.next.next

        node, index = head, 1
        while node:
            if index & 1 == 0 and node.random:
                node.random = node.random.next
            index += 1
            node = node.next

        copy = head.next
        node1, node2 = head, copy
        while node2 and node2.next:
            node1.next = node1.next.next
            node2.next = node2.next.next
            node1 = node1.next
            node2 = node2.next

        return copy


if __name__ == "__main__":
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)

    head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None
    node1.random = None
    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node1

    s = Solution()
    copy = s.copyRandomList(head)
    print(copy)
