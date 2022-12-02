# %%
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        balls = []
        n = len(boxes)
        for i in range(n):
            if boxes[i] == "1":
                balls.append(i)
        res = [0] * n
        for i in range(n):
            res[i] = sum([abs(x - i) for x in balls])
        return res
