# %%
from typing import List


class Solution:

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float(inf)
        res = []
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if min_diff > diff:
                min_diff = diff
                res = []
                res.append(arr[i:i + 2])
            elif min_diff == diff:
                res.append(arr[i:i + 2])
            else:
                pass
        return res