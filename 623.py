# Definition for a binary tree node.
# %%
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, root, d):
        if root is None:
            return
        if d == self.depth - 1:
            root.left = TreeNode(self.val, root.left, None)
            root.right = TreeNode(self.val, None, root.right)
            return
        self.dfs(root.left, d + 1)
        self.dfs(root.right, d + 1)

    def addOneRow(self, root, val: int, depth: int):
        self.val = val
        self.depth = depth
        if depth == 1:
            root.left = TreeNode(root.val, root.left,root.right)
            root.val = val
            root.right = None
        else:
            self.dfs(root, 1)
        return root


a = Solution()
root = TreeNode(1)
a.addOneRow(root, 2, 1)