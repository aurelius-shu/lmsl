#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
60. 把二叉树打印成多行

广度优先遍历，只是要记录当前行需要打印的数量
'''

from binarytree import TreeNode
from collections import deque
import sys


def print_binarytree(root):
    if not root:
        return

    nodes = deque()
    nodes.append(root)
    # 当前行要打印的结点数
    tobeprinted = 1
    # 下一行要打印的结点数
    nextLevel = 0
    while nodes:
        node = nodes.popleft()
        # print(node.value, end=' ')
        sys.stdout.write(str(node.value) + ' ')

        if node.left:
            nodes.append(node.left)
            nextLevel += 1
        if node.right:
            nodes.append(node.right)
            nextLevel += 1
        tobeprinted -= 1

        # 当前行打印结束时，换行，切把下一行的打印结点数赋给当前行打印结点数
        if tobeprinted == 0:
            print('\n')
            tobeprinted = nextLevel
            nextLevel = 0


if __name__ == '__main__':
    root = TreeNode(8)
    node1 = TreeNode(6)
    node2 = TreeNode(10)
    node3 = TreeNode(5)
    node4 = TreeNode(7)
    node5 = TreeNode(9)
    node6 = TreeNode(11)

    root.left = node1
    root.right = node2

    node1.left = node3
    node1.right = node4

    node2.left = node5
    node2.right = node6

    print_binarytree(root)
