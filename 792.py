# %%
from typing import List
from collections import Counter


class Solution:
    def isSubseq(self, s, s1):
        i = j = 0
        while i < len(s) and j < len(s1):
            if s[i] == s1[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j == len(s1) and i <= len(s)

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        cnt = 0
        words = Counter(words)
        for word in words:
            if self.isSubseq(s, word):
                cnt += words[word]
        return cnt
