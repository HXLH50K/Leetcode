class Solution:
    def minPartitions(self, n: str) -> int:
        res = 0
        while n:
            if n[-1] == "9":
                return 9
            res = max(res, int(n[-1]))
            n = n[:-1]
        return res
