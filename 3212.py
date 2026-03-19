from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        new_grid = [[{"X": 0, "Y": 0, ".": 0} for _ in range(n)] for _ in range(m)]

        # first cell
        new_grid[0][0][grid[0][0]] = 1

        # first row
        for j in range(1, n):
            for c in "XY.":
                new_grid[0][j][c] = new_grid[0][j - 1][c]
            new_grid[0][j][grid[0][j]] += 1

        # first column
        for i in range(1, m):
            for c in "XY.":
                new_grid[i][0][c] = new_grid[i - 1][0][c]
            new_grid[i][0][grid[i][0]] += 1

        # rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                for c in "XY.":
                    new_grid[i][j][c] = (
                        new_grid[i - 1][j][c]
                        + new_grid[i][j - 1][c]
                        - new_grid[i - 1][j - 1][c]
                    )
                new_grid[i][j][grid[i][j]] += 1

        count = 0
        for i in range(m):
            for j in range(n):
                if (
                    new_grid[i][j]["X"] > 0
                    and new_grid[i][j]["Y"] == new_grid[i][j]["X"]
                ):
                    count += 1
        return count
