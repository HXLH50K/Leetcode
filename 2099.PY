from collections import Counter, defaultdict


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        candidates = defaultdict(int)
        for key, value in sorted(cnt.items(), key=lambda x: -x[0]):
            if k <= 0:
                break
            if value > 0:
                candidates[key] = min(value, k)
                k -= candidates[key]
        res = []
        for x in nums:
            if x in candidates and candidates[x] > 0:
                res.append(x)
                candidates[x] -= 1
        return res
