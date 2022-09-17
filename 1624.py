from collections import defaultdict


class Solution:

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        alphabet = defaultdict(list)
        for i in range(len(s)):
            alphabet[s[i]].append(i)
        res = -1
        for k in alphabet:
            res = max(res, max(alphabet[k]) - min(alphabet[k]) - 1)
        return res