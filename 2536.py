from typing import List
import numpy as np


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = np.zeros((n, n), dtype=int)
        for r1, c1, r2, c2 in queries:
            mat[r1 : r2 + 1, c1 : c2 + 1] += 1
        return mat.tolist()
