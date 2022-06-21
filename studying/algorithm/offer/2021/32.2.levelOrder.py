# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self._q1 = []
        self._q2 = []

    def levelOrder(self, root):
        if not root:
            return []

        result = []
        self._q1.append(root)
        while self._q1 or self._q2:
            row = []
            run = False
            while self._q1:
                run = True
                node = self._q1[0]
                row.append(node.val)
                if node.left:
                    self._q2.append(node.left)
                if node.right:
                    self._q2.append(node.right)
                self._q1 = self._q1[1:]

            while not run and self._q2:
                node = self._q2[0]
                row.append(node.val)
                if node.left:
                    self._q1.append(node.left)
                if node.right:
                    self._q1.append(node.right)
                self._q2 = self._q2[1:]
            result.append(row)
        return result
