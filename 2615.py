from typing import List
from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        loc_map = defaultdict(list)
        for i, num in enumerate(nums):
            loc_map[num].append(i)
        res = [0] * len(nums)
        for locs in loc_map.values():
            if len(locs) == 1:
                continue
            total = sum(locs)
            prefix = 0
            n = len(locs)
            for i, loc in enumerate(locs):
                l_sum = i * loc - prefix
                r_sum = (total - prefix - loc) - (n - i - 1) * loc
                res[loc] = l_sum + r_sum
                prefix += loc
        return res