from typing import List
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        summ = sum(nums)
        F = [None]*n
        F[0] = sum(i * nums[i] for i in range(n))

        for i in range(1,n):
            F[i] = F[i-1] + summ - n * nums[n-i]
        return max(F)