class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * n
        # Record the boundary changes
        for l, r in queries:
            diff[l] -= 1
            if r + 1 < n:
                diff[r + 1] += 1

        # Calculate cumulative effect
        count = 0
        for i in range(n):
            count += diff[i]
            if nums[i] + count > 0:
                return False
        return True
