from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        i = start
        res = float("inf")
        while i < len(nums):
            if nums[i] == target:
                res = min(res, abs(i - start))
                break
            i += 1
        i = start
        while i >= 0:
            if nums[i] == target:
                res = min(res, abs(i - start))
                break
            i -= 1
        return res if res != float("inf") else -1
