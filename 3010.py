from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        candis = [float("inf"), float("inf")]
        for x in nums[1:]:
            if x < candis[1]:
                candis[1] = x
                candis.sort()
        return nums[0] + sum(candis)
