#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-20
19. 二叉树的镜像

测试用例：
功能测试：普通二叉树，没有左／右子结点，只有一个结点的二叉树
异常输入测试：根结点为none
'''


from binarytree import TreeNode


# 传入的是可变对象，相当于C中的引用传递
def mirrorrecursively(treeHead):
    if treeHead == None:
        return
    if treeHead.left == None and treeHead.right == None:
        return

    temp = treeHead.left
    treeHead.left = treeHead.right
    treeHead.right = temp

    mirrorrecursively(treeHead.left)
    mirrorrecursively(treeHead.right)


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

    print(treeRoot)

    mirrorrecursively(treeRoot)

    print(treeRoot)
