# %%
import math


class Solution:
    def __init__(self):
        self.MOD = 10**9 + 7

    def fastPow(self, base, p):
        res = 1
        while p > 0:
            if p & 1 == 1:
                res = res * base % self.MOD
            p //= 2
            base = base**2 % self.MOD
        return res % self.MOD

    def countGoodNumbers(self, n: int) -> int:
        return (
            self.fastPow(4, math.floor(n / 2)) * self.fastPow(5, math.ceil(n / 2))
        ) % self.MOD


a = Solution()
a.countGoodNumbers(4)

# %%
