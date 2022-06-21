# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head, k):
        if not head:
            return head

        pre, node = head, head
        while k - 1:
            if not pre.next:
                return None
            pre = pre.next
            k -= 1
        while pre.next:
            pre = pre.next
            node = node.next
        return node
