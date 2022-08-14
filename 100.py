class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preOrder(self, p, q):
        if not self.flag:
            return
        if not p and not q:
            return
        if not p or not q:
            self.flag = False
            return
        if p.val != q.val:
            self.flag = False
            return
        self.preOrder(p.left, q.left)
        self.preOrder(p.right, q.right)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        self.flag = True
        self.preOrder(p, q)
        return self.flag
