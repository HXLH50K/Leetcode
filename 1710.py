# %%
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        res = 0
        while truckSize >= 0 and boxTypes:
            box = boxTypes.pop(0)
            if box[0] <= truckSize:
                res += box[0] * box[1]
            else:
                res += truckSize * box[1]
            truckSize -= box[0]
        return res
