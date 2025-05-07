# %%
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        dp = [[float("inf") for _ in range(m)] for _ in range(n)]
        dp[0][0] = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0] + 1, moveTime[i][0] + 1)
        for j in range(1, m):
            dp[0][j] = max(dp[0][j - 1] + 1, moveTime[0][j] + 1)
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = max(
                    moveTime[i][j] + 1, min(dp[i - 1][j] + 1, dp[i][j - 1] + 1)
                )
        return dp[-1][-1]


# %%
moveTime = [[56, 93], [3, 38]]
Solution().minTimeToReach(moveTime)
