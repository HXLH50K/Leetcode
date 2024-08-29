class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res = 0
        for i, x in enumerate(s):
            res += abs(i - t.index(x))
        return res
