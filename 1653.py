class Solution:
    def minimumDeletions(self, s: str) -> int:
        left_b = [0]
        right_a = [0]
        cnt_b = 0
        for c in s:
            if c == "b":
                cnt_b += 1
            left_b.append(cnt_b)
        cnt_a = 0
        for c in reversed(s):
            if c == "a":
                cnt_a += 1
            right_a.append(cnt_a)
        right_a.reverse()
        res = float("inf")
        for i in range(len(s) + 1):
            res = min(res, left_b[i] + right_a[i])
        return res
