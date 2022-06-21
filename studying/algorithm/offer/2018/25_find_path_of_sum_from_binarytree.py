#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-22
25. 二叉树中和为某一值的路径

测试用例：
功能测试：输入的值在二叉树中有一个／多个或零个复合条件的路径
特殊输入测试：输入空树
'''


from binarytree import TreeNode


def findpath(tree, expsum):
    if tree == None:
        return

    cursum = 0
    path = []
    findpathcore(tree, expsum, path, cursum)


def findpathcore(tree, expsum, path, cursum):
    path.append(tree.value)
    cursum += tree.value

    isLeaf = tree.left == None and tree.right == None
    if expsum == cursum and isLeaf:
        print('path found:', path)

    if tree.left != None:
        findpathcore(tree.left, expsum, path, cursum)

    if tree.right != None:
        findpathcore(tree.right, expsum, path, cursum)

    path.pop()


if __name__ == '__main__':
    tree = TreeNode(10)
    tree.left = TreeNode(5)
    tree.right = TreeNode(12)
    left = tree.left
    left.left = TreeNode(4)
    left.right = TreeNode(7)

    findpath(tree, 22)
