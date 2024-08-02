# %%
from typing import List


class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cnt = 0
        row_1 = [0] * n
        col_1 = [0] * m
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    row_1[i] += 1
                    col_1[j] += 1
        for i in range(n):
            if row_1[i] <= 1:
                continue
            for j in range(m):
                if col_1[j] <= 1:
                    continue
                if grid[i][j] != 1:
                    continue
                cnt += (row_1[i] - 1) * (col_1[j] - 1)

        return cnt


grid = [[1, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
print(Solution().numberOfRightTriangles(grid))  # 13
