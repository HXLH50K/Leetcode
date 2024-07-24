# %%
from typing import List
from collections import Counter


class Solution:
    def relocateMarbles(
        self, nums: List[int], moveFrom: List[int], moveTo: List[int]
    ) -> List[int]:
        stones = Counter(nums)
        for i in range(len(moveFrom)):
            if moveFrom[i] == moveTo[i]:
                continue
            stones[moveTo[i]] += stones[moveFrom[i]]
            stones[moveFrom[i]] = 0
        res = []
        for k, v in stones.items():
            if v > 0:
                res.extend([k])
        res.sort()
        return res


stones = [3, 4]
moveFrom = [4, 3, 1, 2, 2, 3, 2, 4, 1]
moveTo = [3, 1, 2, 2, 3, 2, 4, 1, 1]

Solution().relocateMarbles(stones, moveFrom, moveTo)
