#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-20
模拟 二叉树
'''


from collections import deque


class TreeNode(object):

    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

    def __str__(self):
        if self == None:
            return None
        node = self
        strs = [node._value]
        queue = deque()
        if node._left != None:
            queue.append(node._left)
        if node._right != None:
            queue.append(node._right)

        while queue:
            node = queue.popleft()
            strs.append(node.value)
            if node._left != None:
                queue.append(node._left)
            if node._right != None:
                queue.append(node._right)
        return '->'.join([str(ch) for ch in strs])

    __repr__ = __str__

    @property
    def value(self):
        return self._value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right


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
