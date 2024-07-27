# %%
class Solution:
    def distanceToa(self, s: str) -> int:
        a = ord("a")
        return min(ord(s) - a, a - ord(s) + 26)

    def getSmallestString(self, s: str, k: int) -> str:
        res = ""
        for c in s:
            dist = self.distanceToa(c)
            if dist <= k:
                k -= dist
                res += "a"
            else:
                res += chr(ord(c) - k)
                k = 0
        return res


s = "xaxcd"
k = 4
print(Solution().getSmallestString(s, k))  # aaaaa
