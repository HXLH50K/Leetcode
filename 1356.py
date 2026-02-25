from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        arr = [bin(x)[2:] for x in arr]
        arr.sort(key=lambda x: x.count("1"))
        return [int(x, 2) for x in arr]
