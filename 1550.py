# %%
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        tmp = [x & 1 for x in arr[:3]]
        if not 0 in tmp:
            return True
        for i in range(3, len(arr)):
            tmp.pop(0)
            tmp.append(arr[i] & 1)
            if not 0 in tmp:
                return True
        return False


arr = [102, 780, 919, 897, 901]
Solution().threeConsecutiveOdds(arr)
