# %%
from typing import List
from collections import defaultdict


class Solution:
    def isTimeDiffLowerHour(self, t1, t2):
        h1, m1 = map(int, t1.split(":"))
        h2, m2 = map(int, t2.split(":"))
        if h2 == h1:
            return True
        if h2 - h1 >= 2:
            return False
        if m2 - m1 <= 0:
            return True
        return False

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        dic = defaultdict(list)
        n = len(keyName)
        res = []
        for i in range(n):
            name = keyName[i]
            time = keyTime[i]
            dic[name].append(time)
        for k in dic:
            times = sorted(dic[k])
            if len(times) < 3:
                continue
            for i in range(len(times) - 2):
                if self.isTimeDiffLowerHour(times[i], times[i + 2]):
                    res.append(k)
                    break
        return sorted(res)


keyName = ["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"]
keyTime = ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]
Solution().alertNames(keyName, keyTime)

# %%
