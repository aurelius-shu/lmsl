#-*- coding:utf-8 -*-
"""
题目：
    32 - II. 从上到下打印二叉树 II
    从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

    例如:
    给定二叉树: [3,9,20,null,null,15,7],

     3
    / \
   9  20
      /  \
     15   7
    返回其层次遍历结果：

    [
    [3],
    [9,20],
    [15,7]
    ]

思路：
挨层处理，两个队列隔层记录每一层，

注意：
1. 迭代行时，先添加 row 中的项，再判断是否将 row 添加到 res 中
2. 因为 queue 添加了 None 的项，最后一行为空 []，需手动去除
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []

        queue_first, queue_second, res = [], [], []
        queue_first.append(root)
        is_first = True
        row = []

        while queue_first or queue_second:
            if is_first:
                cur = queue_first.pop(0)
                if cur:
                    queue_second.append(cur.left)
                    queue_second.append(cur.right)
                    row.append(cur.val)
                if not queue_first:
                    is_first = False
                    res.append(row)
                    row = []
            else:
                cur = queue_second.pop(0)
                if cur:
                    queue_first.append(cur.left)
                    queue_first.append(cur.right)
                    row.append(cur.val)
                if not queue_second:
                    is_first = True
                    res.append(row)
                    row = []
        res.pop()
        return res


if __name__ == "__main__":
    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)

    s = Solution()
    res = s.levelOrder(t)
    print(res)