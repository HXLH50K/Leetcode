# %%
from typing import List
from collections import defaultdict


class Solution:

    def sequenceReconstruction(self, nums: List[int],
                               sequences: List[List[int]]) -> bool:
        d = defaultdict(set)
        for seq in sequences:
            for i in range(1, len(seq)):
                d[seq[i - 1]].add(seq[i])
        for i in range(1, len(nums)):
            if nums[i] not in d[nums[i - 1]]:
                return False
        return True