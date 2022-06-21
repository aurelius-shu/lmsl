#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-23
27. 二叉搜索树转双向链表

测试用例：
功能测试：输入一个完全二叉搜索树，一个不含左子/右子结点的二叉搜索树，一各单节点的二叉树
异常输入测试：输入空树
'''


from binarytree import TreeNode


def convert(tree, smaller):
    if tree == None:
        return

    # 叶子结点
    if tree.left == None and tree.right == None:
        return tree

    # 左子树
    left = None
    if tree.left != None:
        left = convert(tree.left, True)

    # 右子树
    right = None
    if tree.right != None:
        right = convert(tree.right, False)

    tree.left = left
    left.right = tree

    tree.right = right
    right.left = tree

    if smaller:
        while tree.right != None:
            tree = tree.right
    else:
        while tree.left != None:
            tree = tree.left

    return tree


if __name__ == '__main__':
    tree = TreeNode(5)
    tree.left = TreeNode(3)
    tree.right = TreeNode(7)

    left = tree.left
    right = tree.right
    left.left = TreeNode(2)
    left.right = TreeNode(4)
    right.left = TreeNode(6)
    right.right = TreeNode(8)

    doublylist = convert(tree, False)

    list1 = [doublylist.value]
    while doublylist.right != None:
        doublylist = doublylist.right
        list1.append(doublylist.value)

    list2 = [doublylist.value]
    while doublylist.left != None:
        doublylist = doublylist.left
        list2.append(doublylist.value)

    print('list1:', list1)
    print('list2:', list2)

