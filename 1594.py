from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7
        dp = [[(0, 0)] * n for _ in range(m)]
        dp[0][0] = (grid[0][0], grid[0][0])
        # first row
        for j in range(1, n):
            dp[0][j] = (dp[0][j - 1][0] * grid[0][j], dp[0][j - 1][1] * grid[0][j])
        # first column
        for i in range(1, m):
            dp[i][0] = (dp[i - 1][0][0] * grid[i][0], dp[i - 1][0][1] * grid[i][0])
        # rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                max_product = max(
                    (dp[i - 1][j][0] * grid[i][j]),
                    (dp[i][j - 1][0] * grid[i][j]),
                    (dp[i - 1][j][1] * grid[i][j]),
                    (dp[i][j - 1][1] * grid[i][j]),
                )
                min_product = min(
                    (dp[i - 1][j][0] * grid[i][j]),
                    (dp[i][j - 1][0] * grid[i][j]),
                    (dp[i - 1][j][1] * grid[i][j]),
                    (dp[i][j - 1][1] * grid[i][j]),
                )
                dp[i][j] = (max_product, min_product)

        result = dp[m - 1][n - 1][0]
        return result % MOD if result >= 0 else -1
