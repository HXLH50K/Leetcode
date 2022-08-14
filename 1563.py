# %%
from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        if n <= 1:
            return 0
        pre_sum = [stoneValue[0]] + [0] * (n - 1)
        for i in range(1, n):
            pre_sum[i] = pre_sum[i - 1] + stoneValue[i]
        dp = [[0] * n for _ in range(n)]


a = Solution()
# a.stoneGameV([6, 2, 3, 4, 5, 5])
# a.stoneGameV([4, 4, 4, 3, 4, 5])
a.stoneGameV([68, 75, 25, 50, 34, 29, 77, 1, 2, 69])

# %%
