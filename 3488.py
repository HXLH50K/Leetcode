from typing import List
from collections import defaultdict
import bisect


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        locs = defaultdict(list)
        for i, x in enumerate(nums):
            locs[x].append(i)
        n = len(nums)
        min_dist = [None] * n
        for i, x in enumerate(nums):
            if len(locs[x]) == 1:
                min_dist[i] = -1
                continue

            # curr_loc = locs[x].index(i) # use binary search here to find the current location of i in locs[x]
            # do bin-search here
            curr_loc = bisect.bisect_left(locs[x], i)

            locs[x].append(locs[x][0] + n)
            locs[x].insert(0, locs[x][-2] - n)
            curr_loc += 1

            min_d = min(
                abs(i - locs[x][curr_loc - 1]),
                abs(locs[x][(curr_loc + 1)] - i),
            )
            min_dist[i] = min_d
        return [min_dist[q] for q in queries]
