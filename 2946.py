from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        k %= n
        new_mat = [row[:] for row in mat]
        for i in range(m):
            if i & 1 == 1:
                new_mat[i] = mat[i][n - k :] + mat[i][: n - k]
                continue
            if i & 1 == 0:
                new_mat[i] = mat[i][k:] + mat[i][:k]
        for i in range(m):
            if new_mat[i] != mat[i]:
                return False
        return True
