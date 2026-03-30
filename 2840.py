from collections import Counter


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1_odd = Counter([x for i, x in enumerate(s1) if i % 2 == 1])
        s1_even = Counter([x for i, x in enumerate(s1) if i % 2 == 0])
        s2_odd = Counter([x for i, x in enumerate(s2) if i % 2 == 1])
        s2_even = Counter([x for i, x in enumerate(s2) if i % 2 == 0])
        return s1_odd == s2_odd and s1_even == s2_even
