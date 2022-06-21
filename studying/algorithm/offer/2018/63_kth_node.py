#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
63. 二叉搜索树的第k个结点

中序遍历到第k个结点即可
'''

from binarytree import TreeNode


# 在递归中，不变类型（如int，string，tuple）的值无法在调用栈之间传递
global k


def kth_node(root, kth):
    global k
    k = kth
    if not root or k == 0:
        return None
    return kth_node_core(root)


def kth_node_core(root):
    global k
    target = None
    # 遍历左结点
    if root.left:
        target = kth_node_core(root.left)

    # 若没有找到target, 则减小k，如果k等于1，说明到了第k大的数
    if not target:
        if k == 1:
            target = root
        k -= 1

    # 若没有找到target，则继续找右结点
    if root.right and not target:
        target = kth_node_core(root.right)

    return target


if __name__ == '__main__':
    root = TreeNode(5)
    node1 = TreeNode(3)
    node2 = TreeNode(7)
    node3 = TreeNode(2)
    node4 = TreeNode(4)
    node5 = TreeNode(6)
    node6 = TreeNode(8)

    root.left = node1
    root.right = node2

    node1.left = node3
    node1.right = node4

    node2.left = node5
    node2.right = node6

    print(root)
    s = kth_node(root, 6)
    print(s, s.value)
