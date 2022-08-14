# %%
from typing import List


class Solution:
    def dfs(self, x, y):
        deep = 1
        if self.memo[x][y] != -1:
            return self.memo[x][y]
        for i, j in [[x - 1, y], [x, y - 1], [x + 1, y], [x, y + 1]]:
            if 0 <= i < self.m and 0 <= j < self.n and self.matrix[i][
                    j] > self.matrix[x][y]:
                deep = max(deep, self.dfs(i, j) + 1)
        self.memo[x][y] = deep
        return deep

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        maxx = 0
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.memo = [[-1 for _ in range(self.n)] for _ in range(self.m)]
        self.matrix = matrix
        for i in range(self.m):
            for j in range(self.n):
                maxx = max(maxx, self.dfs(i, j))
        return maxx


a = Solution()
print(a.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
print(a.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]))
# %%
