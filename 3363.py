class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        mid = []
        lb = [[0] * n for _ in range(n)]
        rt = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                fruit = fruits[i][j]
                if i == j:
                    mid.append(fruit)
                    continue
                if i > j and i >= n - j - 1:
                    lb[i][j] = fruit
                if i < j and j >= n - i - 1:
                    rt[i][j] = fruit
        lb_dp = [[0] * n for _ in range(n)]
        lb_dp[n - 1][0] = fruits[n - 1][0]
        for j in range(1, n):
            for i in range(n):
                lb_dp[i][j] = lb[i][j] + max(
                    lb_dp[i][j - 1],
                    lb_dp[i - 1][j - 1] if i > 0 else 0,
                    lb_dp[i + 1][j - 1] if i != n - 1 else 0,
                )

        rt_dp = [[0] * n for _ in range(n)]
        rt_dp[0][n - 1] = fruits[0][n - 1]
        for i in range(1, n):
            for j in range(n):
                rt_dp[i][j] = rt[i][j] + max(
                    rt_dp[i - 1][j],
                    rt_dp[i - 1][j - 1] if j > 0 else 0,
                    rt_dp[i - 1][j + 1] if j != n - 1 else 0,
                )
        return sum(mid) + rt_dp[-1][-1] + lb_dp[-1][-1]
