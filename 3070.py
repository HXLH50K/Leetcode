from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        # first row
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        # first column
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
        # rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += grid[i - 1][j] + grid[i][j - 1] - grid[i - 1][j - 1]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] <= k:
                    count += 1
        return count
