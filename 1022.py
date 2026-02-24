# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def __init__(self):
        self.nums = []

    def dfs(self, node: Optional[TreeNode], path: str):
        if node is None:
            self.nums.append("0")
            return
        path += str(node.val)
        if node.left is None and node.right is None:
            self.nums.append(path)
            return
        self.dfs(node.left, path)
        self.dfs(node.right, path)

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, "")
        return sum(int(num, 2) for num in self.nums)
