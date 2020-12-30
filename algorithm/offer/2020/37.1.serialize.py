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
先序遍历+后续遍历

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
        def preorder(node):
            data = []
            if not node:
                return data

            data.append(node.val)
            data.extend(preorder(node.left))
            data.extend(preorder(node.right))
            return data

        def inorder(node):
            data = []
            if not node:
                return data

            data.extend(inorder(node.left))
            data.append(node.val)
            data.extend(inorder(node.right))
            return data

        return preorder(root), inorder(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        preorder, inorder = data

        def deserialize(preorder, inorder):
            if preorder:
                root = TreeNode(preorder[0])
                index = inorder.index(root.val)
                root.left = deserialize(preorder[1:index + 1], inorder[:index])
                root.right = deserialize(preorder[index + 1:],
                                         inorder[index + 1:])
                return root

        return deserialize(preorder, inorder)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))