class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        if n & 1:
            mid = s[n // 2]
        s = s[:n // 2]
        s = list(s)
        s.sort()
        s = "".join(s)
        if n & 1:
            return s + mid + s[::-1]
        return s + s[::-1]
        