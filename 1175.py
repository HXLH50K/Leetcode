# %%
import math


class Solution:

    def countPrimes(self, n):
        if n <= 1:
            return 0
        end = int((n + 1)**0.5) + 1
        prime = [False] * 2 + [True] * (n - 1)
        for i in range(2, end):
            if not prime[i]:
                continue
            else:
                prime[i * i:(n + 1):i] = [False] * len(prime[i * i:(n + 1):i])
        return sum(prime)

    def numPrimeArrangements(self, n: int) -> int:
        primes = self.countPrimes(n)
        non_primes = n - primes
        return math.factorial(primes) * math.factorial(non_primes) % (10**9 +
                                                                      7)


a = Solution()
a.numPrimeArrangements(100)
# %%
