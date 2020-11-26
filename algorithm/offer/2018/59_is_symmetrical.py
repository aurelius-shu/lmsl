#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
59. 对称的二叉树

1. 定义一种前序遍历的对称遍历算法，即先遍历右子结点，再遍历左子结点，考虑到树的结构问题，叶子结点指向的Null也放入遍历序列中
2. 递归法：左子树的左子结点与右子树的右子结点  左子树的右子结点与右子树的左子结点  相同
'''


from binarytree import TreeNode


def is_symmetriacal(treeRoot):
    if not treeRoot:
        return True
    return is_symmetriacal_core(treeRoot, treeRoot)


def is_symmetriacal_core(root1, root2):
    # 终止条件
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.value != root2.value:
        return False
    # 左子树的左子结点与右子树的右子结点
    return is_symmetriacal_core(root1.left, root2.right) and is_symmetriacal_core(root1.right, root2.left)


if __name__ == '__main__':
    root = TreeNode(8)
    node1 = TreeNode(6)
    node2 = TreeNode(6)
    # node2 = TreeNode(9)
    node3 = TreeNode(5)
    node4 = TreeNode(7)
    node5 = TreeNode(7)
    node6 = TreeNode(5)

    # node1 = TreeNode(7)
    # node2 = TreeNode(7)
    # # node2 = TreeNode(9)
    # node3 = TreeNode(7)
    # node4 = TreeNode(7)
    # node5 = TreeNode(7)
    # # node6 = TreeNode(5)

    root.left = node1
    root.right = node2

    node1.left = node3
    node1.right = node4

    node2.left = node5
    node2.right = node6

    print(root)
    print(is_symmetriacal(root))
