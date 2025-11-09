class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        n = bin(n)[2:]
        res = 0
        for i, c in enumerate(n):
            if c == "1":
                loc = i
                break
        n = n[loc:]
        cnt_0 = n.count("0")
        res = cnt_0 + len(n) - 1
        return res
