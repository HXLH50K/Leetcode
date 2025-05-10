# %%
from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zero1 = nums1.count(0)
        zero2 = nums2.count(0)
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        if sum1 == sum2 and zero1 == zero2:
            return sum1 + zero1
        if sum1 == sum2 and zero1 != zero2:
            if zero1 == 0 or zero2 == 0:
                return -1
            return sum1 + max(zero1, zero2)
        if sum1 > sum2:
            diff = sum1 - sum2
            if zero2 == 0 or zero1 == 0 and sum2 + zero2 > sum1:
                return -1
            return max(sum2 + zero2, sum1 + zero1)
        if sum1 < sum2:
            diff = sum2 - sum1
            if zero1 == 0 or zero2 == 0 and sum1 + zero1 > sum2:
                return -1
            return max(sum2 + zero2, sum1 + zero1)


nums1 = [20, 0, 18, 11, 0, 0, 0, 0, 0, 0, 17, 28, 0, 11, 10, 0, 0, 15, 29]
nums2 = [16, 9, 25, 16, 1, 9, 20, 28, 8, 0, 1, 0, 1, 27]
Solution().minSum(nums1, nums2)
