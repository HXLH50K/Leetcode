from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[float("inf")] * n for _ in range(n)]
        dp[0][0] = grid[0][0]
        heap = [(grid[0][0], 0, 0)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while heap:
            t, x, y = heapq.heappop(heap)
            if x == n - 1 and y == n - 1:
                return t
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    nt = max(t, grid[nx][ny])
                    if nt < dp[nx][ny]:
                        dp[nx][ny] = nt
                        heapq.heappush(heap, (nt, nx, ny))
        return dp[n - 1][n - 1]
