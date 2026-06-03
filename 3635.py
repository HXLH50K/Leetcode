from typing import List
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        earliestLandFinishTime = float('inf')
        earliestWaterFinishTime = float('inf')
        for i in range(n):
            landFinishTime = landStartTime[i] + landDuration[i]
            if landFinishTime < earliestLandFinishTime:
                earliestLandFinishTime = landFinishTime
        for j in range(m):
            waterFinishTime = waterStartTime[j] + waterDuration[j]
            if waterFinishTime < earliestWaterFinishTime:
                earliestWaterFinishTime = waterFinishTime
        # play land first
        re_land_first = float('inf')
        for i in range(m):
            if waterStartTime[i] >= earliestLandFinishTime:
                re_land_first = min(re_land_first, waterStartTime[i] + waterDuration[i])
            else:
                re_land_first = min(re_land_first, earliestLandFinishTime + waterDuration[i])
        # play water first
        re_water_first = float('inf')
        for i in range(n):
            if landStartTime[i] >= earliestWaterFinishTime:
                re_water_first = min(re_water_first, landStartTime[i] + landDuration[i])
            else:
                re_water_first = min(re_water_first, earliestWaterFinishTime + landDuration[i])
        return min(re_land_first, re_water_first)
