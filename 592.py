#%%
import math


class Solution:

    def fractionAddition(self, expression: str) -> str:
        expression = expression.replace("-", "+-").split("+")
        sum_n = 0
        m = math.factorial(10)
        for x in expression:
            if x == "":
                continue
            numerator, denominator = map(int, x.split("/"))
            sum_n += int(numerator * m / denominator)
        if sum_n == 0:
            return "0/1"
        a = math.gcd(sum_n, m)
        n, d = sum_n / a, m / a
        return f"{int(n)}/{int(d)}"


a = Solution()
expression = "-1/2+1/2+1/3"
a.fractionAddition(expression)
# %%
