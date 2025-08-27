from typing import List
from collections import defaultdict


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        diags = defaultdict(list)
        n = len(grid)
        for i in range(n):
            for j in range(n):
                diags[i - j].append(grid[i][j])
        for k in diags:
            if k < 0:
                diags[k].sort()
            else:
                diags[k].sort(reverse=True)
        for i in range(n):
            for j in range(n):
                grid[i][j] = diags[i - j].pop(0)
        return grid
