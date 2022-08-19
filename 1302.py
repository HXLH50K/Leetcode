# Definition for a binary tree node.
# %%
from typing import Optional
from build_tree import build_tree
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
            for node in q:
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
# %%
a = Solution()
root = [1,2,3,4,5,None,6,7,None,None,None,None,8]
root = build_tree(root)
a.deepestLeavesSum(root)

# %%
