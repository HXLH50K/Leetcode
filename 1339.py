from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.subtree_sums = []

    def preOrderTreeAndSum(self, node: Optional[TreeNode], total_sum: int) -> int:
        if not node:
            return 0
        left_sum = self.preOrderTreeAndSum(node.left, total_sum)
        right_sum = self.preOrderTreeAndSum(node.right, total_sum)
        current_sum = node.val + left_sum + right_sum
        self.subtree_sums.append(current_sum)
        return current_sum

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        full_sum = self.preOrderTreeAndSum(root, 0)
        target_subtree_sum = full_sum  # target is closest to half of full_sum
        for summ in self.subtree_sums:
            if abs(full_sum - 2 * summ) < abs(full_sum - 2 * target_subtree_sum):
                target_subtree_sum = summ
        mod = 10**9 + 7
        print(target_subtree_sum)
        print(full_sum)
        print(self.subtree_sums)
        return (full_sum - target_subtree_sum) % mod * target_subtree_sum % mod
