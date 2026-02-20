class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = set([2, 3, 5, 7, 11, 13, 17, 19])
        cnt = 0
        for x in range(left, right + 1):
            if bin(x).count("1") in primes:
                cnt += 1
        return cnt
