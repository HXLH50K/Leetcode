from collections import defaultdict
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0
        char_count = defaultdict(int)

        l, r = 0, 0
        while r < n:
            char_count[s[r]] += 1

            while max(char_count.values()) > 2:
                char_count[s[l]] -= 1
                if char_count[s[l]] == 0:
                    del char_count[s[l]]
                l += 1

            max_length = max(max_length, r - l + 1)
            r += 1
        return max_length