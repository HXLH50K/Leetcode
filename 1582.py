#%%
from typing import List


# %%
class Solution:

    def numSpecial(self, mat: List[List[int]]) -> int:
        row_sum = [sum(x) for x in mat]
        col_sum = [sum(x) for x in zip(*mat)]
        res = 0
        for i in range(len(row_sum)):
            for j in range(len(col_sum)):
                if row_sum[i] == 1 and col_sum[j] == 1 and mat[i][j] == 1:
                    res += 1
        return res


a = Solution()
mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
a.numSpecial(mat)

# %%
