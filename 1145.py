# %%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_x(self, p, x):
        if not p:
            return
        if p.val == x:
            return p
        return self.find_x(p.left, x) or self.find_x(p.right, x)

    def countNode(self, root):
        if not root:
            return 0
        return self.countNode(root.left) + self.countNode(root.right) + 1

    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        nodex = self.find_x(root, x)
        left = self.countNode(nodex.left)
        right = self.countNode(nodex.right)
        parent = n - left - right - 1
        return any(_ > n // 2 for _ in [left, right, parent])
