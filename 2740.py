# %%
from typing import List


class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        minn = float("inf")
        for i in range(n - 1):
            if nums[i + 1] - nums[i] < minn:
                minn = nums[i + 1] - nums[i]
        return minn
