from typing import List
import numpy as np


class Solution:
    def reverseSubmatrix(
        self, grid: List[List[int]], x: int, y: int, k: int
    ) -> List[List[int]]:
        grid = np.array(grid)
        sub_grid = grid[x : x + k, y : y + k]
        sub_grid = np.flip(sub_grid, axis=0)
        grid[x : x + k, y : y + k] = sub_grid
        return grid.tolist()
