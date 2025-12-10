from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        first_complexity = complexity[0]
        n = len(complexity)
        for c in complexity[1:]:
            if c <= first_complexity:
                return 0
        MOD = 10**9 + 7
        res = 1
        for i in range(2, n):
            res = (res * i) % MOD
        return res
