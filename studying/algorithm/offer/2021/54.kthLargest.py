# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.k = 0

    def kthLargest(self, root, k):
        if not root or not k:
            return None
        self.k = k
        return self.traverse(root).val

    def traverse(self, node):
        if node.right:
            res = self.traverse(node.right)
            if res:
                return res
        self.k -= 1
        if self.k == 0:
            return node
        if node.left:
            res = self.traverse(node.left)
            if res:
                return res
        return None
