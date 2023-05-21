# %%
from typing import List
import math


class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        if max(vat) == 0:
            return 0
        i = 0
        n = len(bucket)
        arr = []
        for j in range(n):
            if vat[j] == 0:
                continue
            if bucket[j] == 0:
                i += 1
                bucket[j] += 1
            arr.append([vat[j], bucket[j], math.ceil(vat[j] / bucket[j])])
        arr.sort(key=lambda x: -x[2])
        res = float("inf")
        for _ in range(10000):
            re = max([x[2] for x in arr]) + i
            if re < res:
                res = re
            i += 1
            arr[0][1] += 1
            arr[0][2] = math.ceil(arr[0][0] / arr[0][1])
            arr.sort(key=lambda x: -x[2])
        return res


bucket = [0, 1, 2]
vat = [0, 0, 1]
Solution().storeWater(bucket, vat)

# %%
