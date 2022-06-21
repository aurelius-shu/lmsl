# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self._paths = []

    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        path = []
        if not root:
            return self._paths
        self.FindPathCore(root, expectNumber, path)
        sorted(self._paths, lambda x, y: len(y) - len(x))
        return self._paths

    def FindPathCore(self, node, num, path):
        path.append(node.val)
        num -= node.val
        if num == 0 and not node.left and not node.right:
            tmp = [x for x in path]
            self._paths.append(tmp)
        if node.left:
            self.FindPathCore(node.left, num, path)
        if node.right:
            self.FindPathCore(node.right, num, path)
        path.pop()
        num += node.val


if __name__ == '__main__':
    s = Solution()
    s.FindPath({}, 22)
