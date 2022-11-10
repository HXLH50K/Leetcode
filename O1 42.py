# %%
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = r = 0
        res = -float('inf')
        pre_sum = [0]
        for x in nums:
            pre_sum.append(pre_sum[-1] + x)
        while l < len(nums) and r < len(nums):
            r += 1
            temp = pre_sum[r] - pre_sum[l]
            res = max(temp, res)
            if temp <= 0:
                l = r

        return res


a = Solution()
a.maxSubArray([60, -30, 27, 100])

# %%
