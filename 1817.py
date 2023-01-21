# %%
from collections import defaultdict
from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dic = defaultdict(set)
        for id_, time in logs:
            dic[id_].add(time)
        res = [0] * k
        for k in dic:
            res[len(dic[k]) - 1] += 1
        return res
