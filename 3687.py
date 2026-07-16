from typing import List
class Solution:
    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
    
    def gcdSum(self, nums: List[int]) -> int:
        n = len(nums)
        prefixGCD = [0] * n
        curr_max = 0
        for i in range(n):
            curr_max = max(curr_max, nums[i])
            prefixGCD[i] = self.gcd(curr_max, nums[i])
        
        prefixGCD.sort()
        i = 0
        j = n - 1
        total_sum = 0
        while i < j:
            total_sum += self.gcd(prefixGCD[i], prefixGCD[j])
            i += 1
            j -= 1
        return total_sum