from typing import List


class Solution:
    def isStrictlyIncreasing(self, s: str) -> bool:
        for i in range(1, len(s)):
            if s[i] < s[i - 1]:
                return False
        return True

    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        res = 0
        for i in range(n):
            column = "".join([strs[j][i] for j in range(len(strs))])
            if not self.isStrictlyIncreasing(column):
                res += 1
        return res
