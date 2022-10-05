# %%
from typing import List
from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic =defaultdict(int)
        for cpdomain in cpdomains:
            cnt, domain = cpdomain.split(" ")
            d = domain.split(".")
            for i in range(len(d)):
                dic[".".join(d[i:])] += int(cnt)
        res = []
        for k in dic:
            res.append(f"{dic[k]} {k}")
        return res