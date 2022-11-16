# %%
from typing import List


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for i, x in enumerate(nums):
            if abs(i - x) > 1:
                return False
        return True
