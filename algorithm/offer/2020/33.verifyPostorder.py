#-*- coding:utf-8 -*-
"""
题目：
    33. 二叉搜索树的后序遍历序列
    输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

    参考以下这颗二叉搜索树：

         5
        / \
       2   6
      / \
     1   3
    示例 1：

    输入: [1,6,3,2,5]
    输出: false
    示例 2：

    输入: [1,3,2,6,5]
    输出: true
     

    提示：

    数组长度 <= 1000
    
思路：
    后续序列的最后一位是子树的根节点

注意：
    分段的起始节点
    遍历比较的起始节点
"""


class Solution:
    def verifyPostorder(self, postorder) -> bool:
        def split(start, end):
            if end - start < 1:
                return True
            root = postorder[end]
            mid = start - 1
            while mid < end and root > postorder[mid + 1]:
                mid += 1
            for i in range(mid + 1, end):
                if postorder[i] < root:
                    return False
            return split(start, mid) and split(mid + 1, end - 1)

        return split(0, len(postorder) - 1)


s = Solution()
res = s.verifyPostorder([4, 8, 6, 12, 16, 14, 10])
print(res)