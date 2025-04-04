# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_depth = 0
        self.lca = None

    def find_depth(self, node: Optional[TreeNode], depth: int) -> int:
        if not node:
            return depth - 1
        left_depth = self.find_depth(node.left, depth + 1)
        right_depth = self.find_depth(node.right, depth + 1)
        if left_depth == right_depth and left_depth >= self.max_depth:
            self.max_depth = left_depth
            self.lca = node
        return max(left_depth, right_depth)

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.find_depth(root, 0)
        return self.lca
