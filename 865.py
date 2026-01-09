# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.lca = None
        self.max_depth = 0

    def preOrder(self, node: Optional[TreeNode], depth: int) -> int:
        if not node:
            return depth - 1
        node.depth = depth
        self.max_depth = max(self.max_depth, depth)
        left_depth = self.preOrder(node.left, depth + 1)
        right_depth = self.preOrder(node.right, depth + 1)
        if left_depth == right_depth and left_depth >= self.max_depth:
            self.lca = node
        return max(left_depth, right_depth)

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.preOrder(root, 0)
        return self.lca
