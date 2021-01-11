#-*- coding:utf-8 -*-
"""
题目：
    34. 二叉树中和为某一值的路径
    输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

    示例:
    给定如下二叉树，以及目标和 sum = 22，

                 5
                / \
               4   8
              /   / \
             11  13  4
            /  \    / \
           7    2  5   1
    返回:

    [
    [5,4,11,2],
    [5,8,4,5]
    ]
     

    提示：

    节点总数 <= 10000

思路：
采用栈记录先序遍历的当前路径
当节点为叶子节点时，判断是否目标路径，如是，记录路径

注意：
记录路径时需要拷贝一个备份用来记录
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, target: int):
        if not root:
            return []

        def checkPath(node):
            self.stack.append(node.val)

            if not node.left and not node.right:
                if sum(self.stack) == target:
                    self.res.append(self.stack[:])
            if node.left:
                checkPath(node.left)
            if node.right:
                checkPath(node.right)

            self.stack.pop()

        checkPath(root)
        return self.res

    def __init__(self):
        self.res = []
        self.stack = []


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    s = Solution()
    res = s.pathSum(root, 22)
    print(res)