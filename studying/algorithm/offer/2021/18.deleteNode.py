# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        pre, node = None, head
        while node.val != val and node.next:
            pre, node = node, node.next
        if node.val == val:
            if pre:
                pre.next = node.next
            else:
                head = node.next
        return head
