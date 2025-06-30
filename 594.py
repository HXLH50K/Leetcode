from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        res = 0
        for key, value in sorted(cnt.items(), key=lambda x: x[0]):
            if key + 1 in cnt:
                res = max(res, value + cnt[key + 1])
        return res
