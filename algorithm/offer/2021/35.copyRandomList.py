# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head:
            return head

        # 复制
        node = head
        while node:
            copy = Node(node.val, node.next, node.random)
            node.next = copy
            node = copy.next

        copy_head = head.next

        # 拆分
        node = head
        while node:
            copy = node.next
            copy.random = copy.random.next if copy.random else None
            node = node.next.next

        node = head
        while node:
            copy = node.next
            node.next = copy.next
            copy.next = node.next.next if node.next else None
            node = node.next

        return copy_head
