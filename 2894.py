class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        summ = sum(range(1, n + 1))
        num2 = sum([x for x in range(1, n + 1) if x % m == 0])
        num1 = summ - num2
        return num1 - num2
