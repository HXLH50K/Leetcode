# %%
class Solution:
    def reverseBits(self, num: int) -> int:
        res = 0
        re = 0
        for x in bin(num)[2:]:
            if x == '1':
                re += 1
            else:
                res = max(res, re)
                re = 0
        else:
            res = max(re, res)
        return res


a = Solution()
a.reverseBits(12)
# %%
import numpy as np

a = np.array([[1, 2, 3], [2, 3, 1]])
np.argmax(a, axis=1)

# %%
