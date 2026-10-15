from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        diff_cnts = []
        for i in range(n):
            for j in range(i + 1, n + 1):
                sub_arr = nums[i:j]
                diff_cnts.append(len(set(sub_arr)))

        return sum([x**2 for x in diff_cnts])
