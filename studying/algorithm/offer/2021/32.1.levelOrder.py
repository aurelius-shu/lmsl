# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self._q = []

    def levelOrder(self, root):
        if not root:
            return self._q

        self._q.append(root)
        result = []
        while self._q:
            node = self._q[0]
            result.append(node.val)
            if node.left:
                self._q.append(node.left)
            if node.right:
                self._q.append(node.right)
            self._q = self._q[1:]
        return result
