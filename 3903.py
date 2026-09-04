from typing import List


class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left_max = [nums[0]]
        right_min = [nums[-1]]

        for i in range(1, n):
            left_max.append(max(left_max[-1], nums[i]))
        for i in range(n - 2, -1, -1):
            right_min.append(min(right_min[-1], nums[i]))
        right_min.reverse()

        for i in range(n):
            if left_max[i] - right_min[i] <= k:
                return i
        return -1
