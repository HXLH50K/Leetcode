from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        MOD = 12345
        flat_grid = [num for row in grid for num in row]
        pre_product = [1] * (m * n)
        pre_product[0] = flat_grid[0] % MOD
        for i in range(1, m * n):
            pre_product[i] = (pre_product[i - 1] * flat_grid[i]) % MOD
        suf_product = [1] * (m * n)
        suf_product[-1] = flat_grid[-1] % MOD
        for i in range(m * n - 2, -1, -1):
            suf_product[i] = (suf_product[i + 1] * flat_grid[i]) % MOD
        product_matrix = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                idx = i * n + j
                left_product = pre_product[idx - 1] if idx > 0 else 1
                right_product = suf_product[idx + 1] if idx < m * n - 1 else 1
                product_matrix[i][j] = (left_product * right_product) % MOD
        return product_matrix
