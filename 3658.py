class Solution:
    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
    
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_sum = 0
        even_sum = 0
        flag = 1
        for i in range(1, 2 * n + 1):
            if flag:
                odd_sum += i
            else:
                even_sum += i
            flag ^= 1
        return self.gcd(odd_sum, even_sum)