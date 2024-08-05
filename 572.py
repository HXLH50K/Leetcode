# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compare(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        return self.compare(node1.left, node2.left) and self.compare(
            node1.right, node2.right
        )

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        is_sub = self.compare(root, subRoot)
        if is_sub:
            return True
        return bool(root) and (
            self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        )
