# %%
from typing import List
from collections import defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dic = defaultdict(int)
        for dom in dominoes:
            k = str(sorted(dom))
            dic[k] += 1
        res = 0
        for v in dic.values():
            res += v * (v - 1) // 2
        return res


# %%
d = [[1, 2], [2, 1], [3, 4], [5, 6]]
Solution().numEquivDominoPairs(d)

# %%
