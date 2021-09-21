# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root):
        if not root:
            return root

        head, tail = self.toDoubleList(root)
        head.left = tail
        tail.right = head
        return head

    def toDoubleList(self, node):
        if not node.left and not node.right:
            return node, node

        head, tail = node, node
        if node.left:
            leftHead, leftTail = self.toDoubleList(node.left)
            leftTail.right = node
            node.left = leftTail
            head = leftHead
        if node.right:
            rightHead, rightTail = self.toDoubleList(node.right)
            node.right = rightHead
            rightHead.left = node
            tail = rightTail
        return head, tail
