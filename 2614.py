class Solution:
    def isPrime(self, x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n = len(nums)
        diags = [nums[i][i] for i in range(n)]
        inv_diags = [nums[i][n - i - 1] for i in range(n)]
        primes = [x for x in diags + inv_diags if self.isPrime(x)]
        return max(primes) if primes else 0
