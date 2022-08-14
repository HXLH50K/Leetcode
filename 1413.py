# %%
from typing import List


class Solution:

    def minStartValue(self, nums: List[int]) -> int:
        pre_sum = [0]
        start_value = 1
        for x in nums:
            pre_sum.append(pre_sum[-1] + x)
            start_value = max(start_value, -pre_sum[-1] + 1)
        return start_value


a = Solution()
a.minStartValue([-3, 2, -3, 4, 2])

# %%
