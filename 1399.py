from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        dic = defaultdict(int)
        for x in range(1, n + 1):
            dic[sum(map(int, list(str(x))))] += 1
        target = max(dic.values())
        res = 0
        for k, v in dic.items():
            if v == target:
                res += 1
        return res
