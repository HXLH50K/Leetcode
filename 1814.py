# %%
from typing import List
from collections import Counter


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        revs = [int(str(x)[::-1]) for x in nums]
        n = len(nums)
        diff = [nums[i] - revs[i] for i in range(n)]
        dic = Counter(diff)
        res = 0
        for k in dic:
            v = dic[k]
            res += v * (v - 1) / 2
        return int(res % (1e9 + 7))
