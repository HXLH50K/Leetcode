class Solution:
    def maxProduct(self, n: int) -> int:
        n = str(n)
        n = list(n)
        n = list(map(int, n))
        n.sort(reverse=True)
        return n[0] * n[1]