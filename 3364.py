from typing import List
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')
        for k in range(l, r + 1):
            for i in range(len(nums) - k + 1):
                subarray = nums[i:i + k]
                subarray_sum = sum(subarray)
                if subarray_sum < min_sum and subarray_sum > 0:
                    min_sum = subarray_sum
        return min_sum if min_sum != float('inf') else -1