from collections import Counter


class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return set(s).__len__()
