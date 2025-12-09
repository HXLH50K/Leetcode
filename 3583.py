from collections import defaultdict, Counter
from typing import List


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        count = []

        freq_all = Counter(nums)
        freq_left = defaultdict(int)
        freq_right = freq_all.copy()
        freq_left[nums[0]] += 1
        freq_right[nums[0]] -= 1
        for j in range(1, n - 1):
            freq_right[nums[j]] -= 1
            left = freq_left[nums[j] << 1]
            right = freq_right[nums[j] << 1]
            count.append(left * right % MOD)
            freq_left[nums[j]] += 1
        return sum(count) % MOD
