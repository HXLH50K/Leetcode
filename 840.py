from typing import List


class Solution:
    def isMagicSquare(self, grid: List[List[int]], row: int, col: int) -> bool:
        nums = set()
        for i in range(3):
            for j in range(3):
                val = grid[row + i][col + j]
                if val < 1 or val > 9 or val in nums:
                    return False
                nums.add(val)

        target_sum = sum(grid[row][col : col + 3])

        for i in range(3):
            if sum(grid[row + i][col : col + 3]) != target_sum:
                return False

        for j in range(3):
            if sum(grid[row + i][col + j] for i in range(3)) != target_sum:
                return False

        if sum(grid[row + i][col + i] for i in range(3)) != target_sum:
            return False

        if sum(grid[row + i][col + 2 - i] for i in range(3)) != target_sum:
            return False

        return True

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m < 3 or n < 3:
            return 0

        cnt = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if self.isMagicSquare(grid, i, j):
                    cnt += 1
        return cnt
