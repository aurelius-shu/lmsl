#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
62. 序列化二叉树

（递归）（前序遍历）
序列化：可直接用前序遍历的序列表示序列化，给每个指向null的指针赋值‘#’，以便确定二叉树的结构
反序列化：遍历前序遍历序列，第一个为root结点，遇‘#’表示null指针，
'''


from binarytree import TreeNode


# 序列化
def serialize(root):
    # 不能用str 因为str是不可变对象，不能实现传引用
    s = []
    if not root:
        return s

    serializeCore(root, s)
    return ','.join(s)


def serializeCore(root, s):
    if not root:
        s.append('#')
        return s

    tmp = str(root.value)
    s.append(tmp)

    serializeCore(root.left, s)
    serializeCore(root.right, s)


# 全局变量，模拟指针变量
global s


# 反序列化
def deserialize(slist):
    global s
    s = slist
    if not s:
        return None

    root = deserializeCore()
    return root


def deserializeCore():
    global s
    # 存在且为'#'，表示父级是叶子结点，直接返回none
    if s and s[0] == '#':
        s = s[1:]
        return None

    # 否则为数字
    num = int(s[0])
    node = TreeNode(num)
    s = s[1:]
    # 如果s遍历完了，把node结点返回
    if not s:
        return node

    # 否则继续遍历s下一个元素
    node.left = deserializeCore()
    node.right = deserializeCore()
    return node


if __name__ == '__main__':
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(5)
    node5 = TreeNode(6)
    node6 = TreeNode(7)
    node7 = TreeNode(8)
    node8 = TreeNode(9)
    node9 = TreeNode(10)
    node10 = TreeNode(1)

    root.left = node1
    root.right = node2

    node1.left = node3
    node1.right = node4

    node2.left = node5
    node2.right = node6

    node3.left = node7
    node3.right = node8

    node4.left = node9
    node4.right = node10

    print(root)
    s = serialize(root)
    print(s)
    slist = s.split(',')
    # print(slist)
    print(deserialize(slist))
