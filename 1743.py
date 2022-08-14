# %%
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        a = set()
        for x in adjacentPairs:
            for y in x:
                if y in a:
                    a.remove(y)
                else:
                    a.add(y)
        res = []
        head = list(a)[0]
        res.append(head)
        while adjacentPairs != []:
            for pair in adjacentPairs:
                if head in pair:
                    pair.remove(head)
                    head = pair[0]
                    res.append(head)
                    adjacentPairs.remove(pair)
        return res


a = Solution()
a.restoreArray([[4, -2], [1, 4], [-3, 1]])
# %%
