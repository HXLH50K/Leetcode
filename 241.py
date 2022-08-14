# %%
from typing import List


class Solution:

    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        for i, x in enumerate(expression):
            if x in ["+", "-", "*"]:
                res1 = self.diffWaysToCompute(expression[:i])
                res2 = self.diffWaysToCompute(expression[i + 1:])
                for a in res1:
                    for b in res2:
                        res.append(eval(str(a) + x + str(b)))
        if not res:
            res.append(int(expression))
        return res


a = Solution()
a.diffWaysToCompute("2*3-4*5")

# %%
