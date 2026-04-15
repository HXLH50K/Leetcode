from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target:
            return 0

        res = float("inf")
        n = len(words)
        i = startIndex + 1
        while i % n != startIndex:
            if words[i % n] == target:
                res = min(res, abs(i - startIndex))
                break
            i += 1

        j = startIndex - 1
        while j % n != startIndex:
            if words[j % n] == target:
                res = min(res, abs(j - startIndex))
                break
            j -= 1
        return res if res != float("inf") else -1
