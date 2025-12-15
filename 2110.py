from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        smooth_descents_areas = [1]
        for i in range(1, n):
            if prices[i - 1] - prices[i] == 1:
                smooth_descents_areas[-1] += 1
            else:
                smooth_descents_areas.append(1)
        res = 0
        for area in smooth_descents_areas:
            res += area * (area + 1) // 2
        return res
