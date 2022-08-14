# %%
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            tmp = "".join(sorted(s))
            if tmp in res:
                res[tmp].append(s)
            else:
                res.update({tmp: [s]})
        return list(res.values())


a = Solution()
a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# %%
