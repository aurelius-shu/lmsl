# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def __init__(self):
        self._result = []

    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return self._result
        if not head.next:
            self._result.append(head.val)
            return self._result
        self.reversePrint(head.next)
        self._result.append(head.val)
        return self._result
