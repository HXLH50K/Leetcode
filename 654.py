# %%
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def constructMaximumBinaryTree(self,
                                   nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        loc = nums.index(max(nums))
        root = TreeNode(nums[loc])
        root.left = self.constructMaximumBinaryTree(nums[:loc])
        root.right = self.constructMaximumBinaryTree(nums[loc + 1:])
        return root


a = Solution()
nums = [3, 2, 1, 6, 0, 5]
root = a.constructMaximumBinaryTree(nums)
# %%
