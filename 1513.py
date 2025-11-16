from collections import Counter


class Solution:
    def numSub(self, s: str) -> int:
        s = s.split("0")
        mod = 10**9 + 7
        s = [len(x) for x in s]
        freq = Counter(s)
        res = 0
        for k, v in freq.items():
            res += (k * (k + 1) // 2) * v
            res %= mod
        return res
