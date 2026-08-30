from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minn = float("inf")
        maxx = float("-inf")
        minn_index = -1
        maxx_index = -1
        n = len(nums)
        for i in range(n):
            if nums[i] < minn:
                minn = nums[i]
                minn_index = i
            if nums[i] > maxx:
                maxx = nums[i]
                maxx_index = i

        left = min(minn_index, maxx_index)
        right = max(minn_index, maxx_index)

        res1 = right + 1
        res2 = n - left
        res3 = left + 1 + n - right

        return min(res1, res2, res3)
