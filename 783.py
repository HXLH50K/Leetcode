# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, leftmin=None, rightmax=None):
        self.val = val
        self.left = left
        self.right = right
        self.leftmin = leftmin
        self.rightmax = rightmax

from typing import Optional
class Solution:
    def dfs(self, node):
        if not node:
            return
        if node.left:
            self.dfs(node.left)
            node.leftmin = node.left.leftmin
            self.res = min(self.res, node.val-node.left.rightmax)
        else:
            node.leftmin = node.val
        if node.right:
            self.dfs(node.right)
            node.rightmax = node.right.rightmax
            self.res = min(self.res, node.right.leftmin-node.val)
        else:
            node.rightmax = node.val

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.res = float('inf')
        self.dfs(root)
        return self.res
