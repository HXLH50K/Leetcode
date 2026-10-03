class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s == "":
            return 0
        dp = [0 for _ in range(len(s))]
        for i in range(len(dp)):
            if s[i] == '(' :
                dp[i] = 0
            elif s[i] == ')' :
                if i == 0:
                    dp[i] = 0
                elif s[i-1] == '(' :
                    if i-2 >= 0:
                        dp[i] = dp[i-2] + 2 #要保证i - 2 >= 0
                    else:
                        dp[i] = 2
                elif s[i-1] == ')' and s[i-dp[i-1]-1] == '(' :
                    if i-dp[i-1]-1>=0:
                        dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2 #要保证i - dp[i - 1] - 2 >= 0
                    elif i-1>=0:
                        dp[i] = 0
                    else:
                        dp[i] = 0
            # print(dp)
        return max(dp)