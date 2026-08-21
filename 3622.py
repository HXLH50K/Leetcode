class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [int(d) for d in str(n)]
        sum_of_digits = sum(digits)
        product_of_digits = 1
        for d in digits:
            product_of_digits *= d
        return n % (sum_of_digits + product_of_digits) == 0
