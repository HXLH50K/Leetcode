# %%
from typing import List
from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dict1 = Counter(arr1)
        res = []
        res_ex = []
        for k in arr2:
            res.extend([k] * dict1[k])
        for k in dict1:
            if k not in arr2:
                res_ex.extend([k] * dict1[k])
        res_ex.sort()
        res.extend(res_ex)
        return res
