# %%
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        i, j = 0, n - 1
        for i in range(n):
            dp[i][i] = piles[i]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(piles[i] - dp[i + 1][j],
                               piles[j] - dp[i][j - 1])
        return dp[0][-1] > 0


a = Solution()
b = a.stoneGame([5, 30, 4])
import numpy as np

print(np.array(b))
# %%
