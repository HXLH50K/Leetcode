from typing import List
from collections import defaultdict
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        n -= 1
        freq = defaultdict(int)
        for i in range(1,n+1):
            freq[i] = 1
        freq[n] += 1
        for num in nums:
            if num not in freq:
                return False
            freq[num] -= 1
        return all(x == 0 for x in freq.values())