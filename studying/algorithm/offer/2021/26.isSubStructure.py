# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A, B):
        if not B or not A:
            return False

        if self.isSubStructureCore(A, B):
            return True

        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def isSubStructureCore(self, A, B):

        if not B:
            return True
        if not A:
            return False

        if A.val == B.val:
            return self.isSubStructureCore(A.left, B.left) and self.isSubStructureCore(A.right, B.right)

        return False
