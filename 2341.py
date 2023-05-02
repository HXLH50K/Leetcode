# %%
from collections import Counter
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        res = [0, 0]
        for k in dic:
            v = dic[k]
            res[0] += v // 2
            res[1] += v & 1
        return res
