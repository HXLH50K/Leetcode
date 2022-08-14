# %%
class Solution:
    def tribonacci(self, n: int) -> int:
        a = [0, 1, 1]
        if n < 3:
            return a[n]
        for _ in range(n-2):
            a.append(sum(a))
            a.pop(0)
        return a[-1]
a = Solution()
a.tribonacci(4)
# %%
