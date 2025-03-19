from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        c = Counter(nums)
        res = [[] for _ in range(max(c.values()))]
        while c:
            k, v = c.popitem()
            for i in range(v):
                res[i].append(k)
        return res
