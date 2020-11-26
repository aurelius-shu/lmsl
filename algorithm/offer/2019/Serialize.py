# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


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
            strs.append(node.val)
            if node._left != None:
                queue.append(node._left)
            if node._right != None:
                queue.append(node._right)
        return '->'.join([str(ch) for ch in strs])

    __repr__ = __str__

    @property
    def val(self):
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


class Solution:
    def __init__(self):
        self._s = []

    def Serialize(self, root):
        # write code here
        if not root:
            return ''
        self._s = [str(root.val)]
        self.SerializeCore(root.left)
        self.SerializeCore(root.right)
        return '!'.join(self._s)

    def SerializeCore(self, node):
        if not node:
            self._s.append('#')
            return
        self._s.append(str(node.val))
        self.SerializeCore(node.left)
        self.SerializeCore(node.right)

    def Deserialize(self, s):
        # write code here
        if not s:
            return None
        self._slist = s.split('!')
        print(self._slist)
        return self.DeserializeCore()

    def DeserializeCore(self):
        if not self._slist:
            return None
        if self._slist and self._slist[0] == '#':
            self._slist.pop(0)
            return None
        print(self._slist[0])
        node = TreeNode(int(self._slist.pop(0)))
        node.left = self.DeserializeCore()
        node.right = self.DeserializeCore()
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
    s = Solution()
    res = s.Serialize(root)
    print(res)

    tree = s.Deserialize(res)
    print(tree)
