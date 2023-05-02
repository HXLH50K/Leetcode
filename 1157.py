# %%
from typing import List
from collections import defaultdict


class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.d = defaultdict(list)
        for i, x in enumerate(arr):
            self.d[x].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        Round = 30
        for _ in range(Round):
            choice = self.arr[random.randint(left, right)]
            l = bisect_left(self.d[choice], left)
            r = bisect_right(self.d[choice], right)
            if r - l >= threshold:
                return choice
        return -1
