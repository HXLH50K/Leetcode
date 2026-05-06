from typing import List
import numpy as np
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0]) if m > 0 else 0
        for row in boxGrid:
            barriers_loc = []
            for i in range(n):
                if row[i] == '*':
                    barriers_loc.append(i)
            barriers_loc.append(n)
            barriers_loc.insert(0, -1)
            for i in range(1, len(barriers_loc)):
                left = barriers_loc[i-1] + 1
                right = barriers_loc[i] - 1
                row[left:right+1] = sorted(row[left:right+1], key=lambda x: x == '#')
        return np.rot90(boxGrid, k=-1).tolist()