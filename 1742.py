# %%
from collections import defaultdict
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        dic = defaultdict(int)
        for i in range(lowLimit, highLimit+1):
            dic[sum(map(int, list(str(i))))] += 1
        return max(dic.values())

Solution().countBalls(1,10)
# %%
