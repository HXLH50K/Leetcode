# %%
from typing import List
from collections import Counter


class Solution:

    def frequencySort(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        eles = sorted(sorted(dic.items(), key=lambda x: x[0], reverse=True), key=lambda x: x[1])
        res = []
        for e, n in eles:
            res += [e] * n
        return res


a = Solution()
nums = [2, 3, 1, 3, 2]
a.frequencySort(nums)
# %%
