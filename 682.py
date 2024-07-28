# %%
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        log = []
        for i, op in enumerate(operations):
            if op == "+":
                log.append(log[-1] + log[-2])
            elif op == "D":
                log.append(log[-1] * 2)
            elif op == "C":
                log.pop()
            else:
                log.append(int(op))
        return sum(log)


Solution().calPoints(["5", "2", "C", "D", "+"])
