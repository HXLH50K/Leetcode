from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        for num, count in sorted(Counter(arr).items(), reverse=True):
            if num == count:
                return num
        return -1
