class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # 预处理所有子串是否为回文串
        isPalindrome = [[False] * n for _ in range(n)]

        # 初始化单个字符和两个字符的情况
        for i in range(n):
            isPalindrome[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                isPalindrome[i][i + 1] = True

        # 处理长度大于2的子串
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and isPalindrome[i + 1][j - 1]:
                    isPalindrome[i][j] = True

        # dp[i]表示前i个字符的最小分割次数
        dp = [float("inf")] * n

        for i in range(n):
            if isPalindrome[0][i]:
                dp[i] = 0
                continue

            for j in range(i):
                if isPalindrome[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n - 1]
