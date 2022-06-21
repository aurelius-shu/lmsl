# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        lengthA, lengthB = self.length(headA), self.length(headB)
        nodeA, nodeB = headA, headB

        if lengthA > lengthB:
            step = lengthA - lengthB
            while step:
                nodeA = nodeA.next
                step -= 1
        elif lengthB > lengthA:
            step = lengthB - lengthA
            while step:
                nodeB = nodeB.next
                step -= 1

        while nodeA:
            if nodeA == nodeB:
                return nodeA
            nodeA, nodeB = nodeA.next, nodeB.next
        return None

    def length(self, node):
        if not node:
            return 0
        count = 0
        while node:
            count += 1
            node = node.next
        return count
