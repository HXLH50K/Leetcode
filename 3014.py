from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        pref = Counter(word)
        values = list(pref.values())
        values.sort(reverse=True)
        ans = 0
        for i in range(len(values)):
            if i // 8 == 0:
                ans += values[i]
                continue
            if i // 8 == 1:
                ans += values[i] * 2
                continue
            if i // 8 == 2:
                ans += values[i] * 3
                continue
            if i // 8 == 3:
                ans += values[i] * 4
                continue
            assert False, "Should not reach here"
        return ans