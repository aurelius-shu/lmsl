# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        mirror = self.mirror(root)
        return self.equal(root, mirror)

    def equal(self, n1, n2):
        if not n1 and not n2:
            return True
        if not n1 or not n2:
            return False

        if n1.val == n2.val:
            return self.equal(n1.left, n2.left) and self.equal(n1.right, n2.right)
        return False

    def mirror(self, node):
        if not node:
            return node

        nnode = TreeNode(node.val)
        nnode.left, nnode.right = self.mirror(node.right), self.mirror(node.left)
        return nnode
