#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-26
39. 二叉树的深度

测试用例：
功能测试：输入一般二叉树，输入没有左子／右子树的二叉树
异常输入测试：二叉树为空，二叉树只有一个结点
'''


from binarytree import TreeNode


# 二叉树的深度
def tree_depth(tree):
    if tree == None:
        return 0

    left = tree_depth(tree.left)
    right = tree_depth(tree.right)

    return left+1 if left > right else right+1


# 二叉树的平衡判断
def is_balance_binarytree(tree):
    if tree == None:
        return True, 0

    left = is_balance_binarytree(tree.left)
    right = is_balance_binarytree(tree.right)
    if left[0] and right[0]:
        dif = left[1]-right[1]
        if dif <= 1 and dif >= -1:
            return True, left[1]+1 if left[1] > right[1] else right[1]+1

    return False, left[1]+1 if left[1] > right[1] else right[1]+1


if __name__ == '__main__':

    # 测试 tree balance
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.left.right=TreeNode(3)

    # tree = None
    print(is_balance_binarytree(tree))

    # 测试 tree depth
    # tree = TreeNode(1)
    # tree.left = TreeNode(2)
    # tree.left.right = TreeNode(3)
    # tree.left.left = TreeNode(4)

    # tree.right = TreeNode(2)
    # tree.right.right = TreeNode(3)
    # tree.right.right.left = TreeNode(4)

    # # tree = None
    # print('depth of this tree:', tree_depth(tree))
