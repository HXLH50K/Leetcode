from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        if len(c) == 1:
            return 0
        cnt = sorted(c.values())
        max_odd = -1
        for i in range(len(cnt) - 1, -1, -1):
            if cnt[i] & 1 == 1:
                max_odd = cnt[i]
                break

        max_even = -1
        for i in range(len(cnt) - 1, -1, -1):
            if cnt[i] & 1 == 0:
                max_even = cnt[i]
                break

        min_odd = -1
        for i in range(len(cnt)):
            if cnt[i] & 1 == 1:
                min_odd = cnt[i]
                break
        min_even = -1
        for i in range(len(cnt)):
            if cnt[i] & 1 == 0:
                min_even = cnt[i]
                break
        return max(max_odd - min_even, -max_even + min_odd)
