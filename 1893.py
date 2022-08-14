# %%
from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int,
                  right: int) -> bool:
        flag = True
        for x in range(left, right + 1):
            tmp_flag = False
            for y in ranges:
                tmp_flag = tmp_flag or (y[0] <= x and y[1] >= x)
                if tmp_flag:
                    break
            flag = flag and tmp_flag
            if not flag:
                break
        return flag


a = Solution()
a.isCovered(ranges=[[1, 2], [3, 4], [5, 6]], left=2, right=5)
a.isCovered(ranges=[[1, 10], [10, 20]], left=21, right=21)

# %%
