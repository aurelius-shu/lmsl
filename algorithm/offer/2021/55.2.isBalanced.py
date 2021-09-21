# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        if not root or (not root.left and not root.right):
            return True
        deep, balance = self.depth(root)
        return balance

    def depth(self, node):
        if not node:
            return 0, True
        left, left_b = self.depth(node.left)
        right, right_b = self.depth(node.right)
        return max(left, right) + 1, (abs(left - right) < 2) and left_b and right_b
