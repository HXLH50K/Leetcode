#%%
from typing import List


class Solution:

    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = set()
        cols = set()
        for indice in indices:
            if indice[0] in rows:
                rows.remove(indice[0])
            else:
                rows.add(indice[0])
            if indice[1] in cols:
                cols.remove(indice[1])
            else:
                cols.add(indice[1])
        res = res = len(rows) * n + len(cols) * m - 2 * len(rows) * len(cols)
        return res


a = Solution()
a.oddCells(2, 3, [[0, 1], [1, 1]])
# %%
