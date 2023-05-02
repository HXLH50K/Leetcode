# %%
from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        hours = [1 if x > 8 else -1 for x in hours]
        n = len(hours)
        presum = [0]
        res = 0
        for x in hours:
            presum.append(presum[-1] + x)
        for i in range(n + 1):
            for j in range(i, n + 1):
                if presum[j] - presum[i] <= 0:
                    continue
                res = max(res, j - i)
        return res


hours = [6, 6, 9]
Solution().longestWPI(hours)

# %%
