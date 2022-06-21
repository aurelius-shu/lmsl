#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-14
6. 重构二叉树

测试用例：
1、普通二叉树（完全二叉树、不完全二叉树）
2、特殊二叉树（所有节点没有右子节点，所有节点没有左子节点，只有一个节点）
3、特殊输入（root 指向空指针，前序遍历序列与中序遍历序列不匹配）
'''


def rebuild_binarytree(preorder, inorder):
    if len(preorder) != len(inorder) or len(preorder) < 1:
        return None

    binarytree = rebuild_core(preorder, inorder, 0,
                              len(preorder)-1, 0, len(inorder)-1)

    print(binarytree)


def rebuild_core(preorder, inorder, preorderstart, preorderend, inorderstart, inorderend):

    # 前序遍历的第一个节点是当前根节点
    rootValue = preorder[preorderstart]
    root = {}
    root[rootValue] = {}
    # root[rootValue]['left'] = {}
    # root[rootValue]['right'] = {}

    # 前序遍历完成
    if preorderstart == preorderend:
        # 中序遍历完成 且 前序与中序的起始位置相同
        if inorderstart == inorderend and preorder[preorderstart] == inorder[inorderstart]:
            return root
        else:
            raise ValueError('Invalid input.')

    # 在中序遍历序列中找到根节点
    rootIndex = inorderstart
    while rootIndex <= inorderend and inorder[rootIndex] != rootValue:
        rootIndex += 1

    if rootIndex == inorderend and inorder[rootIndex] != rootValue:
        raise ValueError('Invalid input.')

    leftLen = rootIndex-inorderstart
    leftPreorderEnd = preorderstart + leftLen
    if leftLen > 0:
        root[rootValue]['left'] = rebuild_core(
            preorder, inorder, preorderstart+1, leftPreorderEnd, inorderstart, rootIndex-1)
    if leftLen < preorderend-preorderstart:
        root[rootValue]['right'] = rebuild_core(
            preorder, inorder, leftPreorderEnd+1, preorderend, rootIndex+1, inorderend)

    return root


if __name__ == '__main__':
    preorder = [1, 2, 4, 7, 3, 5, 6, 8]
    inorder = [4, 7, 2, 1, 5, 3, 8, 6]
    rebuild_binarytree(preorder, inorder)
