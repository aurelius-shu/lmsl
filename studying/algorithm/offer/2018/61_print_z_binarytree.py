#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
61. 按之字打印二叉树

用两个栈隔行保存行的结点，偶数行左先入栈，奇数行右先入栈
'''


from binarytree import TreeNode
from stack import Stack
from collections import deque
import sys


def print_z_binarytree(root):

    if not root:
        return

    # 定义两个栈
    levels = [Stack(), Stack()]
    current = 0
    next = 1

    levels[current].push(root)
    # 当两个栈其中一个不为空
    while((not levels[0].is_empty()) or (not levels[1].is_empty())):
        node = levels[current].pop()
        sys.stdout.write(str(node.value)+' ')

        # 奇数行，左子结点先入栈，右子结点后入栈（即偶数行结点从右到左打印）
        if current == 0:
            if node.left:
                levels[next].push(node.left)
            if node.right:
                levels[next].push(node.right)
        # 偶数行，右子结点先入栈，左子结点后入栈（即奇数行结点从左往右打印）
        else:
            if node.right:
                levels[next].push(node.right)
            if node.left:
                levels[next].push(node.left)

        # 当前行打印完后，切换一下一行为当前行，并将当前行（已空）设置为下一行
        if levels[current].is_empty():
            print('\r\n')
            current = 1-current
            next = 1-next


if __name__ == '__main__':
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(5)
    node5 = TreeNode(6)
    node6 = TreeNode(7)
    node7 = TreeNode(8)
    node8 = TreeNode(9)
    node9 = TreeNode(10)
    node10 = TreeNode(11)

    root.left = node1
    root.right = node2

    node1.left = node3
    node1.right = node4

    node2.left = node5
    node2.right = node6

    node3.left = node7
    node3.right = node8

    node4.left = node9
    node4.right = node10

    print_z_binarytree(root)
