#%%
class Solution:
    def countHomogenous(self, s: str) -> int:
        i = j = 0
        res = 0
        while j < len(s):
            if s[i] == s[j]:
                j += 1
                continue
            res += sum(range(j - i + 1))
            i = j
        res += sum(range(j - i + 1))
        return int(res % (1e9 + 7))
