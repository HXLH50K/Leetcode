# %%
from typing import List
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        while folder:
            tmp = folder.pop(0)
            if res and tmp.startswith(res[-1]) and tmp[len(res[-1])] == '/':
                continue
            res.append(tmp)
        return res