# %%
from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        brackets = [brackets[0]] + [
            [brackets[i][0] - brackets[i - 1][0], brackets[i][1]]
            for i in range(1, len(brackets))
        ]
        for upper, percent in brackets:
            if income <= 0:
                break
            if income >= upper:
                income -= upper
                tax += upper * percent / 100
            else:
                tax += income * percent / 100
                income = 0
        return tax
