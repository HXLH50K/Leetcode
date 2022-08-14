from random import randint, choice
from typing import List


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        if n > 2 * len(blacklist):
            self.s = n - len(blacklist)
            b_lt_s = {i for i in blacklist if i < self.s}
            w_gt_s = {i for i in range(self.s, n)} - set(blacklist)
            self.map = dict(zip(b_lt_s, w_gt_s))
            self.pick = self.pick_small_b
        else:
            self.pool = list(set(range(n)) - set(blacklist))
            self.pick = self.pick_large_b()

    def pick_small_b(self) -> int:
        res = randint(0, self.s - 1)
        return res if res not in self.map else self.map[res]

    def pick_large_b(self) -> int:
        return choice(self.pool)
