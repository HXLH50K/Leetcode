# %%
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        s = map(int, list(s))
        cnt1 = cnt2 = 0
        for i, x in enumerate(s):
            if x != i % 2:
                cnt1 += 1
            else:
                cnt2 += 1
        return min(cnt1, cnt2)


s = "0100"
Solution().minOperations(s)

# %%
