# %%
import numpy as np


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i] = False in [dp[i - j**2] for j in range(1, int(i**0.5) + 1)]

        return dp[-1]


a = Solution()
b = np.array(a.winnerSquareGame(3))
b

# %%
