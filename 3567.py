# %%
from typing import List


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        res = []
        for i in range(m - k + 1):
            re = []
            for j in range(n - k + 1):
                submatrix = set()
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        submatrix.add(grid[x][y])
                submatrix = sorted(submatrix)
                if len(submatrix) == 1:
                    re.append(0)
                    continue
                min_diff = float("inf")
                for x in range(1, len(submatrix)):
                    min_diff = min(min_diff, submatrix[x] - submatrix[x - 1])
                re.append(min_diff)
            res.append(re)
        return res


grid = [[3, -1]]
k = 1
Solution().minAbsDiff(grid, k)
