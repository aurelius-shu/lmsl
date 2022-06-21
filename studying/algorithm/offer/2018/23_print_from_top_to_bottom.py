#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-22
23. 从上往下打印二叉树

测试用例：
输入常规二叉树
输入空的树
'''


from binarytree import TreeNode
from collections import deque


def printfromtoptobottom(tree):
    if tree == None:
        return

    queue = deque()
    queue.append(tree)

    while queue:
        curnode = queue.popleft()

        print(curnode.value)

        if curnode.left:
            queue.append(curnode.left)

        if curnode.right:
            queue.append(curnode.right)


if __name__ == '__main__':
    treeRoot = TreeNode('9')
    treeRoot.left = TreeNode('7')
    treeRoot.right = TreeNode('11')

    left = treeRoot.left
    left.left = TreeNode('6')
    left.right = TreeNode('8')

    right = treeRoot.right
    right.left = TreeNode('10')
    right.right = TreeNode('12')
    right.right.right = TreeNode('13')

    printfromtoptobottom(treeRoot)
    print('------')
    print(treeRoot)
