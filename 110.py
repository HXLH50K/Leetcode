# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def depth(self, root):
        if not root:
            return 0
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
            return -1
        return max(left_depth, right_depth) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)

        return (
            left_depth != -1
            and right_depth != -1
            and abs(left_depth - right_depth) <= 1
        )
