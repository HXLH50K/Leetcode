# %%
from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * (len(questions))
        dp[-1] = questions[-1][0]
        n = len(questions)
        for i in range(n - 2, -1, -1):
            if i + questions[i][1] + 1 >= n:
                dp[i] = max(dp[i + 1], questions[i][0])
            else:
                dp[i] = max(dp[i + 1], questions[i][0] + dp[i + questions[i][1] + 1])
        return dp[0] if dp else 0


questions = [[12, 46], [78, 19], [63, 15], [79, 62], [13, 10]]
solution = Solution()
print(solution.mostPoints(questions))  # Output: 153

# %%
