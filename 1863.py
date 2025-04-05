# %%
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1 << (n)):
            tmp = 0
            print(bin(i))
            for j in range(n):
                if (i >> j) & 1:
                    tmp ^= nums[j]
            ans += tmp
        return ans


# Example usage:
sol = Solution()
result = sol.subsetXORSum([1, 2, 3])

# %%
