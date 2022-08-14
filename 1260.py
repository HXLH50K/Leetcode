# %%
from typing import List
import numpy as np
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        grid = np.array(grid)
        line = grid.flatten()
        n = rows * cols
        k = k % n
        line = np.concatenate((line[n-k:],line[:n-k]),axis=0)
        grid = line.reshape(rows,cols)
        return grid.tolist()

a = Solution()
k = 23
grid  = [[1,2,3],[4,5,6],[7,8,9]]
c = a.shiftGrid(grid, k)


# %%
