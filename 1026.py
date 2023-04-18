from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            root.max = root.val
            root.min = root.val
        elif not root.left:
            self.maxAncestorDiff(root.right)
            root.max = max(root.val, root.right.max)
            root.min = min(root.val, root.right.min)
        elif not root.right:
            self.maxAncestorDiff(root.left)
            root.max = max(root.val, root.left.max)
            root.min = min(root.val, root.left.min)
        else:
            self.maxAncestorDiff(root.left)
            self.maxAncestorDiff(root.right)
            root.max = max(root.val, root.left.max, root.right.max)
            root.min = min(root.val, root.left.min, root.right.min)
        self.res = max(self.res, abs(root.max - root.val), abs(root.min - root.val))
        return self.res
