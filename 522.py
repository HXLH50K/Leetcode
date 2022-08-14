#%%
from typing import List


class Solution:

    def findSubStr(self, s: str) -> List:
        # substrs = []
        # for x in range(len(s)):
        #     for i in range(len(s) - x):
        #         substrs.append(s[i:i + x + 1])
        # substrs.append("")
        # return set(substrs)
        substrs = []
        for i in range(2**len(s)):
            tmp = ""
            for j in range(len(s)):
                if (i >> j) % 2 == 1:
                    tmp += s[j]
            if tmp:
                substrs.append(tmp)
        return substrs
    
    def findLUSlength(self, strs: List[str]) -> int:
        special_substrs = dict()
        for s in strs:
            substrs = self.findSubStr(s)
            for s in substrs:
                if s in special_substrs:
                    special_substrs[s] += 1
                else:
                    special_substrs[s] = 1
        res = -1
        for s in special_substrs:
            res = max(res, len(s)) if special_substrs[s] == 1 else res
        return res


a = Solution()
# a.findLUSlength(["aba","cdc","eae"])
a.findSubStr("abc")
# %%
