class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        sq = n**0.5
        if not sq % 1 == 0:
            return False
        sq = int(sq)
        return sq & (sq - 1) == 0
