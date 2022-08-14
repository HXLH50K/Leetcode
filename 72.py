# %%
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                a = dp[i-1][j-1] \
                    if word1[i-1] == word2[j-1] else dp[i-1][j-1]+1
                b = dp[i - 1][j] + 1
                c = dp[i][j - 1] + 1
                dp[i][j] = min(a, b, c)
                # if word1[i] == word2[j]:
                #     dp[i][j] = dp[i - 1][j - 1]
                # else:
                #     dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j],
                #                        dp[i][j - 1])

        return dp[-1][-1]


a = Solution()
a.minDistance(word1="intention", word2="execution")
# %%
