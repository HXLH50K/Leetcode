from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        if k > min(nums):
            return -1
        return len([x for x in nums if x > k])
