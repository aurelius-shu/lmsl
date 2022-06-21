# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        if not head.next.next:
            tail = head.next
            tail.next = head
            head.next = None
            return tail

        next, node, pre = head, head.next, head.next.next
        next.next = None
        while pre:
            node.next = next
            next, node, pre = node, pre, pre.next
        node.next = next
        return node
