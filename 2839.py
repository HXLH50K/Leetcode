class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1_odd = set([s1[1], s1[3]])
        s1_even = set([s1[0], s1[2]])
        s2_odd = set([s2[1], s2[3]])
        s2_even = set([s2[0], s2[2]])
        return s1_odd == s2_odd and s1_even == s2_even
