from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix_sum[i][j] = (
                    mat[i - 1][j - 1]
                    + prefix_sum[i - 1][j]
                    + prefix_sum[i][j - 1]
                    - prefix_sum[i - 1][j - 1]
                )
        size = min(m, n)
        for k in range(size, 0, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    total = (
                        prefix_sum[i + k][j + k]
                        - prefix_sum[i][j + k]
                        - prefix_sum[i + k][j]
                        + prefix_sum[i][j]
                    )
                    if total <= threshold:
                        return k
        return 0
