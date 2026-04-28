from typing import List
from collections import Counter

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flattened = [num for row in grid for num in row]
        flattened.sort()
        freq = Counter(flattened)
        nums = sorted(freq.keys())
        operations = 0

        target = flattened[len(flattened) // 2]

        for num in nums:
            diff = abs(num - target)
            if diff % x != 0:
                return -1
            operations += (diff // x) * freq[num]
        return operations