from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        res = set()
        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if i == j:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    if digits[k] & 1 != 0:
                        continue
                    res.add(digits[i] * 100 + digits[j] * 10 + digits[k])
        return len(res)
