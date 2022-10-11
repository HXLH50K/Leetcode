class Solution:

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s3 = [(s1[i], s2[i]) for i in range(n) if s1[i] != s2[i]]
        return len(s3) == 0 or len(s3) == 2 and s3[0] == s3[1][::-1]
