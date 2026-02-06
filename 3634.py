from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        n = len(nums)
        i = 0
        j = 1
        while j < n:
            if i == j:
                j += 1
            elif nums[j] > k * nums[i]:
                i += 1
            else:
                j += 1
            res = max(res, j - i)
        return n - res
