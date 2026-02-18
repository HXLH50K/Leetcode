class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = bin(n)[2:]
        bit = 1
        for c in n:
            if int(c) != bit:
                return False
            bit = 1 - bit
        return True
