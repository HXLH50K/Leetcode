# %%
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):
            num = num1 - k * num2
            if num < k or num < 0:
                continue
            count_1 = bin(num).count("1")
            if count_1 <= k:
                return k
        return -1
