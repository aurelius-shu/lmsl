# -*- coding:utf-8 -*-

def ConvertBinaryTreeToList(list, node):
    """
    前序打印
    :param node:
    :return:
    """
    if not root:
        return

    list.append(str(node.val))
    if not not node.left:
        ConvertBinaryTreeToList(list, node.left)
    if not not node.right:
        ConvertBinaryTreeToList(list, node.right)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        list=[]
        ConvertBinaryTreeToList(list, self)
        return ' '.join(list)


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
            return None
        root = TreeNode(pre[0])
        index = tin.index(pre[0])
        self.core(root, pre[1:index + 1], pre[index + 1:], tin[:index], tin[index + 1:])
        return root

    def core(self, node, pre_left, pre_right, tin_left, tin_right):
        if len(tin_left) > 1:
            index = tin_left.index(pre_left[0])
            node.left = TreeNode(pre_left[0])
            self.core(node.left, pre_left[1:index + 1], pre_left[index + 1:], tin_left[:index], tin_left[index + 1:])
        if len(tin_right) > 1:
            index = tin_right.index(pre_right[0])
            node.right = TreeNode(pre_right[0])
            self.core(node.right, pre_right[1:index + 1], pre_right[index + 1:], tin_right[:index],
                      tin_right[index + 1:])
        if len(tin_left) == 1:
            node.left = TreeNode(tin_left[0])
        if len(tin_right) == 1:
            node.right = TreeNode(tin_right[0])




if __name__ == '__main__':
    pre, tin = [1, 2, 3, 4, 5, 6, 7], [3, 2, 4, 1, 6, 5, 7]
    solution = Solution()
    root = solution.reConstructBinaryTree(pre, tin)
    print(root)
