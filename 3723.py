class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res = ""
        while sum > 0:
            max_digit = min(9, sum)
            sum -= max_digit
            num -= 1
            res += str(max_digit)

        if num < 0:
            return ""
        res += "0" * num
        return res
