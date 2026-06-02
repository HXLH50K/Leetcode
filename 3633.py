from typing import List
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        land = sorted([(landStartTime[i], landDuration[i]) for i in range(n)], key=lambda x: x[0])
        water = sorted([(waterStartTime[i], waterDuration[i]) for i in range(m)], key=lambda x: x[0])
        res = float('inf')
        for i in range(n):
            for j in range(m):
                # play land first
                re_land_first = float('inf')
                re_land_first = max(land[i][0] + land[i][1] + water[j][1], water[j][0] + water[j][1])
                # play water first
                re_water_first = float('inf')
                re_water_first = max(water[j][0] + water[j][1] + land[i][1], land[i][0] + land[i][1])
                res = min(res, re_land_first, re_water_first)
        return -1 if res == float('inf') else res