#-*- coding:utf-8 -*-
"""
题目：
    32 - III. 从上到下打印二叉树 III
    请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

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
    [20,9],
    [15,7]
    ]
    
思路：
挨层处理，两个队列隔层记录每一层，
奇数行正向记录，偶数行反向记录

注意：
1. 迭代行时，先添加 row 中的项，再判断是否将 row 添加到 res 中
2. 因为 queue 添加了 None 的项，最后一行为空 []，需手动去除
3. 偶数行因为方向入栈，在奇数行使用时需要从尾部开始遍历
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
                cur = queue_first.pop()
                if cur:
                    queue_second.append(cur.left)
                    queue_second.append(cur.right)
                    row.append(cur.val)
                if not queue_first:
                    is_first = False
                    res.append(row)
                    row = []
            else:
                cur = queue_second.pop()
                if cur:
                    queue_first.append(cur.right)
                    queue_first.append(cur.left)
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