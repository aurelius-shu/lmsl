#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-20
18. 树的子结构

测试用例：
功能测试：两棵普通二叉树，树B是或不是树A的子结构
异常输入测试：树A或树B是none
'''

from binarytree import TreeNode


def hasSubTree(treeRoot1, treeRoot2):
    has = False
    if treeRoot1 != None and treeRoot2 != None:
        if treeRoot1.value == treeRoot2.value:
            has = DoesTree1HaveTree2(treeRoot1, treeRoot2)
        if not has:
            has = hasSubTree(treeRoot1.left, treeRoot2)
        if not has:
            has = hasSubTree(treeRoot1.right, treeRoot2)

    return has


def DoesTree1HaveTree2(tree1, tree2):
    if tree2 == None:
        return True
    if tree1 == None:
        return False
    if tree1.value != tree2.value:
        return False
    return DoesTree1HaveTree2(tree1.left, tree2.left) and DoesTree1HaveTree2(tree1.right, tree2.right)


if __name__ == '__main__':
    tree1 = TreeNode('9')
    tree1.left = TreeNode('7')
    tree1.right = TreeNode('11')

    left = tree1.left
    left.left = TreeNode('6')
    left.right = TreeNode('8')

    right = tree1.right
    right.left = TreeNode('10')
    right.right = TreeNode('12')
    right.right.right = TreeNode('13')

    # tree2 = TreeNode('7')
    # tree2.left = TreeNode('6')
    # tree2.right = TreeNode('8')
    tree2 = None

    print(hasSubTree(tree1, tree2))
