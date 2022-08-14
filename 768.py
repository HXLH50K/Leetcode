# %%
from typing import List


class Solution:

    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 1
        for i in range(1, len(arr) - 1):
            if max(arr[:i]) < min(arr[i:]):
                res += 1
        return res