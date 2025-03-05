class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        # dp[i][j]表示s[i:j+1]是否为回文串
        dp = [[False] * n for _ in range(n)]

        # 初始化所有长度为1的子串都是回文串
        for i in range(n):
            dp[i][i] = True

        # 计算所有可能的回文子串
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if length == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

        # 枚举两个分割点，检查三个子串是否都是回文串
        for i in range(n - 2):  # 第一个分割点
            for j in range(i + 1, n - 1):  # 第二个分割点
                if dp[0][i] and dp[i + 1][j] and dp[j + 1][n - 1]:
                    return True

        return False
