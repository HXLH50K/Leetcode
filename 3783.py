class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - self.reverse(n))
    
    def reverse(self, n: int) -> int:
        return int(str(n)[::-1])