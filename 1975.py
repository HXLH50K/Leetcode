from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        matrix_flat = [num for row in matrix for num in row]
        matrix_flat.sort()
        n = len(matrix_flat)
        for i in range(n - 1):
            if matrix_flat[i] < 0 and matrix_flat[i + 1] < 0:
                matrix_flat[i], matrix_flat[i + 1] = (
                    -matrix_flat[i],
                    -matrix_flat[i + 1],
                )
                i += 1
                continue
            if matrix_flat[i] < 0 and matrix_flat[i + 1] >= 0:
                if abs(matrix_flat[i]) < matrix_flat[i + 1]:
                    break
                else:
                    matrix_flat[i], matrix_flat[i + 1] = (
                        -matrix_flat[i],
                        -matrix_flat[i + 1],
                    )
                    break
        return sum(matrix_flat)
