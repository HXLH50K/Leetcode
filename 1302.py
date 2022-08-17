# Definition for a binary tree node.
# %%
from typing import Optional
# %%
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = [root]
        q1 = []
        while q:
            res = 0
            while q:
                node = q.pop(0)
                res += node.val
                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)
            if len(q1) == 0:
                return res
            q = q1
            q1 = []
        return -1
