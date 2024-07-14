# %%
class Solution:
    def subPali(self, s, k):
        i, j = 0, len(s) - 1
        while i < j:
            if k < 0:
                break
            if s[i] != s[j]:
                k -= 1
            i += 1
            j -= 1
        return k >= 0

    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        res = []
        for l, r, k in queries:
            res.append(self.subPali(s[l : r + 1], k))
        return res
