class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        if n == 0:
            return dp[0]
        dp[1] = costs[0] + 1**2
        if n == 1:
            return dp[1]
        dp[2] = min(dp[1] + costs[1] + 1**2, costs[1] + 2**2)
        if n == 2:
            return dp[2]
        dp[3] = min(dp[2] + costs[2] + 1**2, dp[1] + costs[2] + 2**2, costs[2] + 3**2)
        if n == 3:
            return dp[3]

        for i in range(4, n + 1):
            dp[i] = min(
                dp[i - 1] + costs[i - 1] + 1**2,
                dp[i - 2] + costs[i - 1] + 2**2,
                dp[i - 3] + costs[i - 1] + 3**2,
            )

        return dp[n]
