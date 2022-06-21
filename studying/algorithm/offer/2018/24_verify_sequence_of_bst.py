#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-22
24. 二叉搜索树的后序遍历序列

测试用例：
功能测试：输入后续遍历的序列对应完全二叉树，没有左子／右子结点的二叉树，只有一个界点的二叉树
特殊输入测试：输入空序列
'''

from binarytree import TreeNode


def verify_sequence_of_bst(sequence):
    if not sequence:
        return False

    root = sequence[-1]

    left = []
    right = []
    i = 0
    while sequence[i] < root:
        left.append(sequence[i])
        i += 1

    while sequence[i] > root:
        right.append(sequence[i])
        i += 1

    if sequence[i] != root or i != len(sequence)-1:
        return False

    isleftbst = True
    if left:
        isleftbst = verify_sequence_of_bst(left)

    isrightbst = True
    if right:
        isrightbst = verify_sequence_of_bst(right)

    return isleftbst and isrightbst


if __name__ == '__main__':
    sequence = [5, 7, 6, 9, 11, 10, 8]
    # sequence = [7, 4, 6, 5]
    print('is sequence a bst:', verify_sequence_of_bst(sequence))
