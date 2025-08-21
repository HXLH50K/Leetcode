import numpy as np


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        grid = np.array(grid, dtype=np.int8)
        rows, cols = grid.shape
        top, left = 0, 0
        bottom, right = rows - 1, cols - 1
        while top < rows:
            if grid[top].any():
                break
            top += 1
        while left < cols:
            if grid[:, left].any():
                break
            left += 1
        while bottom >= 0:
            if grid[bottom].any():
                break
            bottom -= 1
        while right >= 0:
            if grid[:, right].any():
                break
            right -= 1
        return (
            (bottom - top + 1) * (right - left + 1)
            if top <= bottom and left <= right
            else 0
        )
