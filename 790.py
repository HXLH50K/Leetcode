# %%
class Solution:
    def numTilings(self, n: int) -> int:
        res = [0, 1, 2, 5] + [0] * (n - 3)
        for i in range(4, n + 1):
            res[i] = (2 * res[i - 1] + res[i - 3]) % (10**9 + 7)
        return res[n]


Solution().numTilings(6)
# %%
