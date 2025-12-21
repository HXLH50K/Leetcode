# %%
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        strs_T = [list(col) for col in zip(*strs)]
        ans = 0
        st = [False] * (n - 1)
        for i in range(m):
            new_st = [False] * (n - 1)
            for j in range(n - 1):
                if st[j]:
                    continue
                if strs_T[i][j] > strs_T[i][j + 1]:
                    ans += 1
                    break
                if strs_T[i][j] < strs_T[i][j + 1]:
                    new_st[j] = True
            else:
                st = [st[k] or new_st[k] for k in range(n - 1)]
            if all(st):
                break
        return ans


strs = ["vdy", "vei", "zvc", "zld"]
Solution().minDeletionSize(strs)

# %%
