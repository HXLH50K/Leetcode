# %%
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfsbuild(self, t):
        if not t:
            return
        self.visited.update({t: False})
        if t.left:
            self.parent_dict.update({t.left: t})
        if t.right:
            self.parent_dict.update({t.right: t})
        self.dfsbuild(t.left)
        self.dfsbuild(t.right)

    def dfssearch(self, t, i, K):
        if not t or i > K or self.visited[t]:
            return
        self.visited[t] = True
        if i == K:
            self.res.append(t.val)
            return
        self.dfssearch(t.left, i + 1, K)
        self.dfssearch(t.right, i + 1, K)
        self.dfssearch(self.parent_dict[t], i + 1, K)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.parent_dict = {root: None}
        self.visited = {}
        self.dfsbuild(root)
        self.res = []
        self.dfssearch(target, 0, k)
        return self.res
