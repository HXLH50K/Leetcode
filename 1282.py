# %%
from typing import List


class Solution:

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupSizes = [(i, x) for i, x in enumerate(groupSizes)]
        groupSizes.sort(key=lambda x: x[1])
        res = []
        while groupSizes:
            t = groupSizes[0][1]
            re = [0] * t
            for i in range(t):
                re[i] = groupSizes.pop(0)[0]
            res.append(re)
        return res