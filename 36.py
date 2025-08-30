import numpy as np
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_np = np.zeros([9, 9], dtype=int, order="C")
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    board_np[i][j] = int(board[i][j])
        for row in board_np:
            if np.any(np.bincount(row)[1:] > 1):
                return False
        for col in board_np.T:
            if np.any(np.bincount(col)[1:] > 1):
                return False
        for i in range(3):
            for j in range(3):
                if np.any(
                    np.bincount(
                        board_np[i * 3 : (i + 1) * 3, j * 3 : (j + 1) * 3].ravel()
                    )[1:]
                    > 1
                ):
                    return False
        return True
