# %%
from typing import List
from collections import defaultdict


class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        n = len(points)
        dic = defaultdict(list)
        for i in range(n):
            dic[max([abs(x) for x in points[i]])].append(s[i])
        li = sorted(dic.items())
        ans = 0
        tags = set()
        for x in li:
            new_tags = x[1]
            an = 0
            for new_tag in new_tags:
                if new_tag in tags:
                    return ans
                tags.add(new_tag)
                an += 1
            ans += an
        return ans


points = [[2, 2], [-1, -2], [-4, 4], [-3, 1], [3, -3]]
s = "abdca"
Solution().maxPointsInsideSquare(points, s)

# %%
