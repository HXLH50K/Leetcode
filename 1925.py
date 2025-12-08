class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for c in range(5, n + 1):
            for a in range(3, int((c * c) ** 0.5) + 1):
                b2 = c * c - a * a
                b = int(b2**0.5)
                if b >= a and b * b == b2 and b <= n:
                    res += 1
        return res * 2
