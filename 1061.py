# %%
from collections import defaultdict


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        mapp = defaultdict(set)
        n = len(s1)
        for i in range(n):
            mapp[s1[i]].add(s2[i])
            mapp[s1[i]].add(s1[i])
            mapp[s2[i]].add(s1[i])
            mapp[s2[i]].add(s2[i])
        for letter in mapp:
            while True:
                new_set = set()
                for x in mapp[letter]:
                    # if x == letter:
                    #     continue
                    new_set.update(mapp[x])
                if new_set == mapp[letter]:
                    break
                mapp[letter] = new_set
        res = ""
        for letter in baseStr:
            if letter in mapp:
                res += min(mapp[letter])
            else:
                res += letter
        return res


s1 = "aaaaaaaaaa"
s2 = "aaaaaaaaaa"
baseStr = "mzpxaabrxo"
print(Solution().smallestEquivalentString(s1, s2, baseStr))  # Output: "hdld"

# %%
