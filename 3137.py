# %%
from typing import List
from collections import defaultdict


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        dic = defaultdict(int)
        n = len(word)
        for i in range(0, n, k):
            dic[word[i : i + k]] += 1
        res = float("inf")
        for key, val in dic.items():
            res = min(res, n // k - val)
        return res


Solution().minimumOperationsToMakeKPeriodic("leetcoleet", 2)  # 3

# %%
