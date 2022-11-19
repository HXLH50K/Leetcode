# %%
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height = 0
        maxx = 0
        for x in gain:
            height += x
            maxx = max(maxx, height)
        return maxx
