# %%
from typing import List
from functools import lru_cache


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        times = [1, 7, 30]
        n = len(days)

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
print(a.mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]))
# %%
