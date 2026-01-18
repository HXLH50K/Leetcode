from typing import List


class Solution:
    def isMagicSquare(self, grid: List[List[int]], x: int, y: int, size: int) -> bool:
        target_sum = sum(grid[x][y : y + size])

        # Check rows
        for i in range(x, x + size):
            if sum(grid[i][y : y + size]) != target_sum:
                return False

        # Check columns
        for j in range(y, y + size):
            if sum(grid[i][j] for i in range(x, x + size)) != target_sum:
                return False

        # Check main diagonal
        if sum(grid[x + i][y + i] for i in range(size)) != target_sum:
            return False

        # Check secondary diagonal
        if sum(grid[x + i][y + size - 1 - i] for i in range(size)) != target_sum:
            return False

        return True

    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_size = min(rows, cols)

        for size in range(max_size, 0, -1):
            for i in range(rows - size + 1):
                for j in range(cols - size + 1):
                    if self.isMagicSquare(grid, i, j, size):
                        return size
        return 1
