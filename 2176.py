from collections import defaultdict


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        d = defaultdict(list)
        for i, x in enumerate(nums):
            d[x].append(i)
        res = 0
        a = []
        for num in d:
            locs = d[num]
            for i in range(len(locs) - 1):
                for j in range(i + 1, len(locs)):
                    if (locs[i] * locs[j]) % k == 0:
                        res += 1
        return res
