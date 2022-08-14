# %%
from typing import List


class Solution:
    def dfs(self, i, x):
        if i >= self.n:
            return 0
        if i + x >= self.n:
            return self.suf_sum[i]

        maxx = float("-inf")
        for x in range(1, 4):
            maxx = max(maxx, self.dfs(i + x, x))
        return maxx

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        self.stoneValue = stoneValue
        self.n = len(stoneValue)
        self.suf_sum = [0 for _ in range(self.n)]
        self.suf_sum[-1] = stoneValue[-1]
        for i in range(self.n - 2, -1, -1):
            self.suf_sum[i] = stoneValue[i] + self.suf_sum[i + 1]
        # return self.dfs(0, 1)
        dp = [float("-inf") for _ in range(self.n + 1)]
        dp[-1] = 0
        for i in range(self.n - 1, -1, -1):
            for j in range(1, 4):
                if i + j >= self.n + 1:
                    break
                dp[i] = max(dp[i], self.suf_sum[i] - dp[i + j])
        if dp[0] * 2 > self.suf_sum[0]:
            res = "Alice"
        elif dp[0] * 2 < self.suf_sum[0]:
            res = "Bob"
        else:
            res = "Tie"
        return dp


a = Solution()
a.stoneGameIII([1, 2, 3, 7])

# %%
