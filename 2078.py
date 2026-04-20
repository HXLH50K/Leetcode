from typing import List
from collections import defaultdict
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        d = defaultdict(list)
        for i, c in enumerate(colors):
            if not d[c]:
                d[c] = [i]
                continue
            if len(d[c]) == 1:
                d[c].append(i)
                continue
            d[c][1] = i # store the min and max index of each color
        res = 0
        for i, house in enumerate(colors):
            for color, idx in d.items():
                if color != house:
                    if len(idx) == 1:
                      res = max(res, abs(idx[0] - i))
                    else:
                      res = max(res, abs(idx[0] - i), abs(idx[1] - i))
        return res
