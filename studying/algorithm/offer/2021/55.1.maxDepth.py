# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self._q = []

    def maxDepth(self, root):
        if not root:
            return 0

        node = root
        deep = 0
        self._q.append(node)
        while self._q:
            deep += 1
            q = self._q
            self._q = []
            while q:
                n = q.pop()
                if n.left:
                    self._q.append(n.left)
                if n.right:
                    self._q.append(n.right)

        return deep
