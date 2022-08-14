# %%
from typing import List


class Solution:

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int],
                    p4: List[int]) -> bool:
        p = [p1, p2, p3, p4]
        dist = set()
        for i in range(len(p) - 1):
            for j in range(i + 1, len(p)):
                dist.add((p[i][0] - p[j][0])**2 + (p[i][1] - p[j][1])**2)
        return len(dist) == 2 and 0 not in dist
