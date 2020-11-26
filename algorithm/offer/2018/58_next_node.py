#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
58. 二叉树的下一个结点

1. 如果一个结点有右子树，那么它的下一个结点就是它的右子树的最左子结点
2. 接着我们分析一下结点没有右子树的情形。如果结点是它父结点的左子结点，那么它的下一个结点就是它的父结点
3. 如果一个结点既没有右子树，并且它还是父结点的右子结点,沿着指向父结点的指针一直向上遍历，直到找到一个是它父结点的左子结点的结点。如果这样的结点存在，那么这个结点的父结点就是我们要找的下一个结点，否则没有下一个结点
'''


from binarytree import TreeNode


def get_next(node):
    if not node:
        return None

    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    elif node.parent:
        parent = node.parent
        while parent and parent.right.value == node.value:
            node = parent
            parent = node.parent
        if parent:
            return parent
    return None
