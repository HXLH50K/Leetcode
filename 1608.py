# %%
from typing import List


class Solution:

    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 1, -1, -1):
            if i + 1 <= nums[i] and (i == len(nums) - 1 or i + 1 > nums[i + 1]):
                return i + 1
        else:
            return -1