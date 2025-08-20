import numpy as np
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:  # signature line preserved
        """Count all-1 square submatrices using iterative 2x2 logical convolution.

        Idea:
        Let present_k be a boolean array where True at (i,j) means a kxk all-1 square
        with top-left at (i,j). For k=1 this is just the matrix itself. A (k+1)x(k+1)
        square exists iff the four adjacent kxk squares forming its corners all exist.
        So we can obtain present_{k+1} by a 2x2 AND over sliding windows of present_k.
        We iteratively shrink the array, summing counts each level. This avoids O(K) full
        convolutions and heavy SciPy overhead; only NumPy boolean operations are used.
        Total operations ~ sum_{k}( (m-k+1)(n-k+1) ), which is acceptable for 300x300.
        """
        if not matrix or not matrix[0]:
            return 0
        # Boolean array of 1-cells
        present = np.array(matrix, dtype=np.uint8) == 1
        total = int(present.sum())  # k = 1 squares
        # Iteratively build larger squares
        while present.shape[0] > 1 and present.shape[1] > 1:
            # 2x2 AND pooling (equivalent to checking convolution with all-ones kernel == 4)
            present = (
                present[:-1, :-1]
                & present[1:, :-1]
                & present[:-1, 1:]
                & present[1:, 1:]
            )
            if not present.any():  # early exit if no larger squares
                break
            total += int(present.sum())
        return total
