class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        result = 1
        for i in range(2, n + 1):
            bin_i = bin(i)[2:]
            bin_result = bin(result)[2:] + bin_i
            result = int(bin_result, 2) % MOD
        return result
