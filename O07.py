# %%
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree1(self, preorder, inorder, t):
        pre_root = 0
        in_root = inorder.index(preorder[0])
        in_left = inorder[:in_root]
        in_right = inorder[in_root + 1:]
        pre_left = preorder[1:1 + len(in_left)]
        pre_right = preorder[1 + len(in_left):]
        if len(pre_left) * len(in_left) > 0:
            t1 = TreeNode(pre_left[0])
            t.left = t1
            self.buildTree1(pre_left, in_left, t1)
        if len(pre_right) * len(in_right) > 0:
            t1 = TreeNode(pre_right[0])
            t.right = t1
            self.buildTree1(pre_right, in_right, t1)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        t = TreeNode(preorder[0])
        self.buildTree1(preorder, inorder, t)
        return t


a = Solution()
t = a.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])

# %%
