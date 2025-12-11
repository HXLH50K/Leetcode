# %%
from typing import List
from collections import defaultdict


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        buildings_row = defaultdict(list)
        buildings_col = defaultdict(list)
        for x, y in buildings:
            buildings_row[x].append(y)
            buildings_col[y].append(x)
        for x in buildings_row:
            buildings_row[x].sort()
        for y in buildings_col:
            buildings_col[y].sort()

        res = 0
        for x in sorted(buildings_row.keys()):
            y_list = buildings_row[x]
            if len(y_list) <= 2:
                continue
            for y in y_list[1:-1]:
                x_list = buildings_col[y]
                if len(x_list) <= 2:
                    continue
                if x_list[0] < x < x_list[-1]:
                    res += 1
        return res


n = 3
buildings = [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]
Solution().countCoveredBuildings(n, buildings)
