from collections import defaultdict


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [nums[i] - i for i in range(n)]
        cnt = defaultdict(int)
        good = 0
        for j in range(n):
            good += cnt[nums[j]]
            cnt[nums[j]] += 1
        return n * (n - 1) // 2 - good
