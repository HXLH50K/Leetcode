from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        row_sum = [sum(row) for row in grid]
        col_sum = [sum(col) for col in zip(*grid)]
        total_sum = sum(row_sum)
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        r_sum = 0
        for i in range(m):
            r_sum += row_sum[i]
            if r_sum == target:
                return True
            if r_sum > target:
                break

        c_sum = 0
        for j in range(n):
            c_sum += col_sum[j]
            if c_sum == target:
                return True
            if c_sum > target:
                break

        return False
