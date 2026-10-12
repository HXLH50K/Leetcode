from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(key=lambda x: -abs(x))
        if n & 1:
            lefts = nums[: n // 2 + 1]
            rights = nums[n // 2 + 1 :]
        else:
            lefts = nums[: n // 2]
            rights = nums[n // 2 :]
        return sum([x**2 for x in lefts]) - sum([x**2 for x in rights])
