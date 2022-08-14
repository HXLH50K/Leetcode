# %%
from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int,
                       stations: List[List[int]]) -> int:
        queue = []
        res = 0
        i = 0
        n = len(stations)
        while startFuel < target:
            while i < n and startFuel >= stations[i][0]:
                queue.append(stations[i][1])
                i += 1
            queue.sort()
            try:
                startFuel += queue.pop()
            except:
                return -1
            res += 1
        return res


a = Solution()
a.minRefuelStops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]])
# %%
