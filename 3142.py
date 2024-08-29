# %%
from typing import List


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        if not grid:
            return False
        if not grid[0]:
            return False
        first_row = grid[0]
        for i in range(1, len(first_row)):
            if first_row[i] == first_row[i - 1]:
                return False
        for i in range(1, len(grid)):
            if not all(x == y for x, y in zip(grid[i], first_row)):
                return False
        return True


grid = [[3, 5, 3], [3, 5, 3], [3, 5, 3]]
print(Solution().satisfiesConditions(grid))  # True
