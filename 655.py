# %%
from typing import List, Optional
from build_tree import TreeNode, build_tree


# %%
class Solution:

    def __init__(self):
        self.depth = 0
        self.tree_layer = defaultdict(list)

    def getDepth(self, root, d):
        if not root:
            self.depth = max(self.depth, d)
            return
        self.getDepth(root.left, d + 1)
        self.getDepth(root.right, d + 1)

    def buildMat(self, d, l, r, root):
        if not root:
            return
        s = str(root.val)
        pos = (l + r) // 2
        self.mat[d][pos] = s
        self.buildMat(d + 1, l, pos, root.left)
        self.buildMat(d + 1, pos, r, root.right)

    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        self.getDepth(root, 0)
        self.length = 2**self.depth - 1
        self.mat = [[""] * self.length for _ in range(self.depth)]
        self.buildMat(0, 0, self.length, root)
        return self.mat


a = Solution()
root = build_tree([1, 2, 3, None, 4])
a.printTree(root)
# %%
