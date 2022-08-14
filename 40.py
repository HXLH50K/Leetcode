# %%
from typing import List


class Solution:
    def bt(self, i, temp):
        if sum(temp) > self.target or i >= self.n:
            return
        if sum(temp) == self.target:
            self.res.append(temp.copy())
            return
        temp.append(self.candidates[i])
        self.bt(i + 1, temp)
        temp.pop()

    def combinationSum2(self, candidates: List[int],
                        target: int) -> List[List[int]]:
        candidates.sort()
        self.candidates = candidates
        self.target = target
        self.n = len(candidates)
        self.res = []
        self.bt(0, [])
        return self.res


a = Solution()
a.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)

# %%
