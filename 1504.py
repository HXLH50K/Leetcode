import numpy as np
from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0
        arr = np.array(mat, dtype=np.int32)
        m, n = arr.shape
        prefix = np.cumsum(arr, axis=0)

        total = 0

        def row_segments_sum(row_bool: np.ndarray) -> int:
            if not row_bool.any():
                return 0
            r = row_bool.view(np.int8)
            diff = np.diff(np.concatenate(([0], r, [0])))
            starts = np.where(diff == 1)[0]
            ends = np.where(diff == -1)[0]
            lengths = ends - starts
            return int(np.sum(lengths * (lengths + 1) // 2))

        zeros_row = np.zeros((1, n), dtype=np.int32)
        for h in range(1, m + 1):
            upper = prefix[h - 1 :]
            lower = np.vstack((zeros_row, prefix[: m - h]))
            sums_h = upper - lower  # shape (m-h+1, n)
            mask = sums_h == h
            for row in mask:
                total += row_segments_sum(row)
        return total
