#-*- coding:utf-8 -*-
"""
题目：
    36. 二叉搜索树与双向链表
    输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

    为了让您更好地理解问题，以下面的二叉搜索树为例：

    我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

    下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。

    特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。

思路：
递归 - 中序遍历
1. 节点无子节点时，将当前节点作为左右节点返回
2. 当节点存在左/右节点时，将左/右节点转成左/右子双链表，并返回链表的头尾节点
3. 将当前节点与左/右子双链表衔接，并移动头尾节点至合并链表的头尾处，返回头尾节点

注意：
"""


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root

        def tree2List(node):
            if not node.left and not node.right:
                return node, node

            if node.left:
                left, right = tree2List(node.left)
                right.right = node
                node.left = right
            if node.right:
                left, right = tree2List(node.right)
                left.left = node
                node.right = left

            left, right = node, node
            while right.right:
                right = right.right
            while left.left:
                left = left.left

            return left, right

        left, right = tree2List(root)
        left.left = right
        right.right = left
        return left