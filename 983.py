# %%
from typing import List
from functools import lru_cache

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        times = [1, 7, 30]
        n = len(days)

        # @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0
            minn = float("inf")
            j = i
            for c, t in zip(costs, times):
                while j < n and days[j] < days[i] + t:
                    j += 1
                minn = min(minn, dp(j) + c)
            return minn

        return dp(0)


a = Solution()
a.mincostTickets([1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,24,25,27,28,29,30,31,34,37,38,39,41,43,44,45,47,48,49,54,57,60,62,63,66,69,70,72,74,76,78,80,81,82,83,84,85,88,89,91,93,94,97,99],
[9,38,134])

# %%
