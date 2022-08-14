# %%
from typing import List


class Solution:
    def dfs(self, i, m):
        if i >= self.n:
            return 0
        if i + 2 * m >= self.n:
            return self.suf_sum[i]
        if (i, m) in self.memo:
            return self.memo[(i, m)]
        maxx = 0
        for x in range(1, 2 * m + 1):
            maxx = max(maxx, self.suf_sum[i] - self.dfs(i + x, max(x, m)))
        self.memo.update({(i, m): maxx})
        return maxx

    def stoneGameII(self, piles: List[int]) -> bool:
        self.n = len(piles)
        self.suf_sum = [0 for _ in range(self.n)]
        self.suf_sum[-1] = piles[-1]
        self.memo = {}
        for i in range(self.n - 2, -1, -1):
            self.suf_sum[i] = self.suf_sum[i + 1] + piles[i]
        """
            way1: DFS
        """
        # return self.dfs(0,1)
        """
            way2: DP
        """
        dp = [[0 for _ in range(self.n + 1)] for _ in range(self.n)]
        for i in range(self.n - 1, -1, -1):
            for m in range(1, self.n + 1):
                if i + 2 * m >= self.n:
                    dp[i][m] = self.suf_sum[i]
                else:
                    for x in range(1, 2 * m + 1):
                        dp[i][m] = max(dp[i][m],
                                       self.suf_sum[i] - dp[i + x][max(x, m)])
        return dp[0][1]
        # dp = [[0 for _ in range(n)] for _ in range(n)]
        # for i in range(n):
        #     dp[i][i] = piles[i]
        # for i in range(n - 1, -1, -1):
        #     for m in range(1, n):
        #         if i + 2 * m > n:
        #             dp[i][m] = suf_sum[i]
        #             continue
        #         for x in range(2 * m):
        #             dp[i][m] = max(suf_sum[i] - dp[i][max(m, x)], dp[i][m])

        # return dp


a = Solution()
b = a.stoneGameII([2, 7, 9, 4, 4])
import numpy as np

print(np.array(b))
# %%
