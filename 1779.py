# %%
from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = -1
        minn = float("inf")
        for i, point in enumerate(points):
            x_, y_ = point
            if x_ == x and minn > abs(y_ - y):
                minn = abs(y_ - y)
                res = i
            if y_ == y and minn > abs(x_ - x):
                minn = abs(x_ - x)
                res = i
        return res
