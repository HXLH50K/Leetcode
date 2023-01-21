# %%
from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [[float("inf")] * 3 for _ in range(n)]
        dp[0] = [1, 0, 1]
        for i in range(1, n):
            for j in range(3):
                if obstacles[i] != j + 1:
                    dp[i][j] = dp[i - 1][j]
            for j in range(3):
                if obstacles[i] != j + 1:
                    dp[i][j] = min(
                        dp[i][j], min([dp[i][x] for x in range(3) if x != j]) + 1
                    )
        return min(dp[-1])
