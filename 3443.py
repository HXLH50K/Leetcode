# %%


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        cnt_N = 0
        cnt_S = 0
        cnt_W = 0
        cnt_E = 0
        res = 0
        for c in s:
            if c == "N":
                cnt_N += 1
            elif c == "S":
                cnt_S += 1
            elif c == "W":
                cnt_W += 1
            elif c == "E":
                cnt_E += 1
            hor_diff = abs(cnt_N - cnt_S)
            ver_diff = abs(cnt_E - cnt_W)
            k_diff = min(k, min(cnt_N, cnt_S) + min(cnt_E, cnt_W))
            re = hor_diff + ver_diff + 2 * k_diff
            res = max(res, re)
        return res


s = "NWSE"
k = 1
print(Solution().maxDistance(s, k))  # Output: 2
