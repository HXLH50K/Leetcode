# %%
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        l = 0
        r = 0
        n = len(nums)
        nums.sort()
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for i in range(n):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]
        return dp[target]


# Example usage:
sol = Solution()
print(sol.canPartition([14, 9, 8, 4, 3, 2]))  # Output: True

# %%
