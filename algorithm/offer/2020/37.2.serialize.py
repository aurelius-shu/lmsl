#-*- coding:utf-8 -*-
"""
题目：
    37. 序列化二叉树
    请实现两个函数，分别用来序列化和反序列化二叉树。

    示例: 

    你可以将以下二叉树：

        1
       / \
      2   3
         / \
        4   5

    序列化为 "[1,2,3,null,null,4,5]"
    
思路：
层序遍历+null

注意：
当节点的值不存在重复时，可以使用先序遍历+后续遍历
当节点的值存在重复时，只能使用层序遍历+null
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue, data = [], []

        if not root:
            return data

        queue.append(root)
        while queue:
            node = queue.pop(0)
            if node:
                data.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                data.append(None)

        return data

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # if data[0] is None:
        if not data:
            return None

        root = TreeNode(data.pop(0))
        queue = [root]
        while data:
            node = queue.pop(0)
            val = data.pop(0)
            if val is not None:
                node.left = TreeNode(val)
                queue.append(node.left)
            val = data.pop(0)
            if val is not None:
                node.right = TreeNode(val)
                queue.append(node.right)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))