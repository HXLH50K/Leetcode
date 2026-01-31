from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for x in letters:
            if x > target:
                return x
        return letters[0]
