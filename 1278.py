class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)

        # 计算将s[i:j+1]变成回文串需要修改的最少字符数
        def cost(i, j):
            count = 0
            while i < j:
                if s[i] != s[j]:
                    count += 1
                i += 1
                j -= 1
            return count

        # dp[i][k]表示将前i个字符分成k段的最小修改次数
        dp = [[float("inf")] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        # 动态规划过程
        for i in range(1, n + 1):
            for m in range(1, min(k + 1, i + 1)):
                # 如果只分成1段
                if m == 1:
                    dp[i][m] = cost(0, i - 1)
                    continue

                # 枚举最后一段的起始位置
                for j in range(m - 1, i):
                    dp[i][m] = min(dp[i][m], dp[j][m - 1] + cost(j, i - 1))

        return dp[n][k]
