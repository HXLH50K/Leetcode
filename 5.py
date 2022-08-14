# %%
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        ans = ""
        maxx = len(ans)
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                elif j - i == 1:
                    dp[i][j] = s[j] == s[i]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[j] == s[i]
                if dp[i][j]:
                    if maxx < j - i + 1:
                        ans = s[i:j + 1]
                        maxx = len(ans)
        return ans


import numpy as np

a = Solution()
print(np.array(a.longestPalindrome("babad")))
# print(a.longestPalindrome("b"))
# print(a.longestPalindrome("baab"))
# print(a.longestPalindrome(""))

# %%
