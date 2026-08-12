from typing import List
from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        i = 0
        bad = 0
        max_len = 0

        for j, x in enumerate(nums):
            freq[x] += 1
            if freq[x] == k + 1:
                bad += 1

            while bad > 0:
                y = nums[i]
                if freq[y] == k + 1:
                    bad -= 1
                freq[y] -= 1
                if freq[y] == 0:
                    del freq[y]
                i += 1

            max_len = max(max_len, j - i + 1)

        return max_len