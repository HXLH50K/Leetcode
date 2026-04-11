from typing import List
from collections import defaultdict


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        nums_to_index = defaultdict(list)
        for i, num in enumerate(nums):
            nums_to_index[num].append(i)
        res = float("inf")
        for num, indices in nums_to_index.items():
            if len(indices) < 3:
                continue
            indices.sort()
            for i in range(len(indices) - 2):
                dist = (
                    abs(indices[i] - indices[i + 2])
                    + abs(indices[i + 1] - indices[i + 2])
                    + abs(indices[i] - indices[i + 1])
                )
                res = min(res, dist)
        return res if res != float("inf") else -1
