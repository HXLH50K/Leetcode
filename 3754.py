# %%
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        nums = list(map(int, list(str(n))))
        summ = sum(nums)
        nums = [x for x in nums if x != 0]
        x = int("".join(map(str, nums)))
        return summ * x

n = 10203040
Solution().sumAndMultiply(n)
# %%
