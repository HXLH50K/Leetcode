from typing import List
from collections import defaultdict
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        value_to_loc_map = defaultdict(list)
        for i,x in enumerate(nums):
            value_to_loc_map[x].append(i)
        min_distance = float('inf')
        for value, locs in value_to_loc_map.items():
            rev_value = int(str(value)[::-1])
            if rev_value not in value_to_loc_map:
                continue
            rev_locs = value_to_loc_map[rev_value]
            for loc in locs:
                for rev_loc in rev_locs:
                    if loc >= rev_loc:
                        continue
                    min_distance = min(min_distance, abs(loc-rev_loc))
        return min_distance if min_distance != float('inf') else -1