#-*- coding:utf-8 -*-
"""
题目：
    28. 对称的二叉树
    请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

    例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

        1
       / \
      2   2
     / \ / \
    3  4 4  3
    但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

        1
       / \
      2   2
       \   \
       3    3

思路：
    递归交换 -> 镜像
    比较

注意：
    制作镜像时注意深拷贝
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isEqual(t1, t2):
            if not t1 and not t2:
                return True

            if t1 and t2 and t1.val == t2.val:
                return isEqual(t1.left, t2.left) and isEqual(
                    t1.right, t2.right)

            return False

        mirror = self.mirrorTree(root)
        return isEqual(root, mirror)

    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        mirror = TreeNode(root.val)
        mirror.left, mirror.right = TreeNode(
            root.right.val) if root.right else None, TreeNode(
                root.left.val) if root.left else None
        mirror.right = self.mirrorTree(root.left)
        mirror.left = self.mirrorTree(root.right)
        return mirror


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)

    s = Solution()
    # mirror = s.mirrorTree(root)
    res = s.isSymmetric(root)
    print(res)