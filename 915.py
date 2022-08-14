# %%
from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        left_max = []
        right_min = []
        for x in nums:
            if not left_max or x > left_max[-1]:
                left_max.append(x)
            else:
                left_max.append(left_max[-1])

        for x in nums[::-1]:
            if not right_min or x < right_min[-1]:
                right_min.append(x)
            else:
                right_min.append(right_min[-1])
        right_min = right_min[::-1]
        for i in range(n - 1):
            if left_max[i] - right_min[i + 1] <= 0:
                return i + 1


a = Solution()
a.partitionDisjoint([5, 0, 3, 8, 6])
# %%
