# %%
from typing import List
import math


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = set()
        m = n = 21
        for i in range(m):
            for j in range(n):
                tmp = x**i + y**j
                if tmp <= bound:
                    res.add(tmp)
        return list(res)


x = 2
y = 3
bound = 10
Solution().powerfulIntegers(x, y, bound)

# %%
