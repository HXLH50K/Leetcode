from collections import defaultdict
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        y_freq = defaultdict(int)
        for x, y in points:
            y_freq[y] += 1
        result = 0
        MOD = 10**9 + 7
        y_freq = [(x * (x - 1) // 2) % MOD for x in y_freq.values() if x >= 2]
        total = sum(y_freq)
        sum_sq = sum(v * v for v in y_freq)
        result = ((total * total - sum_sq) // 2) % MOD
        return result
