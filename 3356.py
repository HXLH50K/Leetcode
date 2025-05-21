class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        k = len(queries)

        # Check if array is already zero
        if all(x == 0 for x in nums):
            return 0

        # Helper function to check if we can make array zero with k queries
        def can_zero_with_k(k_val):
            # Use difference array to calculate reductions
            diff = [0] * (n + 1)
            for j in range(k_val):
                l, r, val = queries[j]
                diff[l] += val
                if r + 1 < n:
                    diff[r + 1] -= val

            # Calculate prefix sum to get total reduction for each position
            curr_sum = 0
            for i in range(n):
                curr_sum += diff[i]
                if nums[i] > curr_sum:
                    return False
            return True

        # Binary search for minimum k
        left, right = 0, k + 1
        while left < right:
            mid = (left + right) // 2
            if can_zero_with_k(mid):
                right = mid
            else:
                left = mid + 1

        return left if left <= k and can_zero_with_k(left) else -1
