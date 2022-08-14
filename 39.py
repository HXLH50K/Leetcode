# %%
from typing import List


class Solution:
    def bt(self, i, temp):
        if sum(temp) > self.target or i >= self.n:
            return
        if sum(temp) == self.target:
            self.res.append(temp)
            return
        self.bt(i, temp + [self.candidates[i]])
        self.bt(i + 1, temp)

    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        self.res = []
        self.target = target
        self.n = len(candidates)
        self.candidates = candidates
        self.bt(0, [])
        return self.res


a = Solution()
a.combinationSum([2, 3, 6, 7], 7)
