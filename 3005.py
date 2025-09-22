from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        values = list(freq.values())
        values.sort(reverse=True)
        maxx = values[0]
        res = maxx
        for i in range(1, len(values)):
            if values[i] == maxx:
                res += maxx
            else:
                break
        return res
