# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = None
        self.row = None
        self.target = 0

    def pathSum(self, root, target):
        if not root:
            return []

        self.result = []
        self.row = []
        self.target = target

        self.pathSumCore(root)
        return self.result

    def pathSumCore(self, node):
        self.row.append(node.val)
        if not node.left and not node.right:
            if sum(self.row) == self.target:
                self.result.append([i for i in self.row])

        if node.left: self.pathSumCore(node.left)
        if node.right: self.pathSumCore(node.right)
        self.row.pop()
