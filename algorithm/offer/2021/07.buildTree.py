# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder:
            return None

        return self.buildNode(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def buildNode(self, preorder, prestart, preend, inorder, instart, inend):
        if not preorder or prestart > preend:
            return None

        node = TreeNode(preorder[prestart])
        if prestart == preend:
            return node

        cur = self.find(preorder[prestart], inorder, instart, inend)

        left_in_start = instart
        left_in_end = cur - 1
        right_in_start = cur + 1
        right_in_end = inend

        left_pre_start = prestart + 1
        left_pre_end = prestart + cur - instart
        right_pre_start = prestart + cur - instart + 1
        right_pre_end = preend

        node.left = self.buildNode(preorder, left_pre_start, left_pre_end, inorder, left_in_start, left_in_end)
        node.right = self.buildNode(preorder, right_pre_start, right_pre_end, inorder, right_in_start, right_in_end)
        return node

    def find(self, target, inorder, start, end):
        cur = start
        while cur <= end and target != inorder[cur]:
            cur += 1
        # todo: 此处需保证 target 存在于 inorder
        return cur

if __name__ == '__main__':
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    s = Solution()
    tree = s.buildTree(preorder, inorder)
    print(tree)