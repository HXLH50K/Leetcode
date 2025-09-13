from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = Counter(s)
        max_vol = 0
        for x in "aiueo":
            max_vol = max(max_vol, freq[x])
        max_novol = 0
        for x in freq:
            if x not in "aiueo":
                max_novol = max(max_novol, freq[x])
        return max_vol + max_novol
