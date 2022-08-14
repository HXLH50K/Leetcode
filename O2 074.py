# %%
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        i = 1
        while True:
            if i < len(intervals) and intervals[i - 1][1] >= intervals[i][0]:
                tmp = [
                    intervals[i - 1][0],
                    max(intervals[i][1], intervals[i - 1][1])
                ]
                for _ in range(2):
                    del intervals[i - 1]
                intervals.insert(i - 1, tmp)
            elif i < len(intervals):
                i += 1
            else:
                break
        return intervals


a = Solution()
a.merge([[1, 4], [0, 4]])

# %%
