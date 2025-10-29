class Solution:
    def smallestNumber(self, n: int) -> int:
        for i in range(1, 11):
            if n <= 2**i - 1:
                return 2**i - 1
        return -1
