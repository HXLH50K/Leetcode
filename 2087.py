from typing import List


class Solution:
    def minCost(
        self,
        startPos: List[int],
        homePos: List[int],
        rowCosts: List[int],
        colCosts: List[int],
    ) -> int:
        res = 0
        for i in range(min(startPos[0], homePos[0]), max(startPos[0], homePos[0]) + 1):
            res += rowCosts[i]
        for i in range(min(startPos[1], homePos[1]), max(startPos[1], homePos[1]) + 1):
            res += colCosts[i]
        return res - rowCosts[startPos[0]] - colCosts[startPos[1]]
