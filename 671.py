# %%
# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, t: TreeNode):
        if t != None:
            self.l.append(t.val)
            self.dfs(t.left)
            self.dfs(t.right)

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.l = []
        self.dfs(root)
        self.l.sort()
        minn = self.l[0]
        for x in self.l:
            if x != minn:
                return x
        else:
            return -1


a = Solution()
