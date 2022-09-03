#%%
from typing import List
# %5
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        res = 1
        point = pairs[0][1]
        for i in range(1, len(pairs)):
            if pairs[i][0] > point:
                point = pairs[i][1]
                res += 1
        return res