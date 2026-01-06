# %%
from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        res = [root.val]
        while q:
            q1 = []
            re = 0
            for x in q:
                if x.left:
                    q1.append(x.left)
                    re += x.left.val
                if x.right:
                    q1.append(x.right)
                    re += x.right.val
            res.append(re)
            q = q1
        res.pop()
        return res.index(max(res)) + 1
