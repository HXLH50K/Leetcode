# %%
class Solution:
    def countAsterisks(self, s: str) -> int:
        flag = True
        res = 0
        for c in s:
            if c == "|":
                flag ^= True
                continue
            if c == "*":
                res += flag
        return res


s = "l|*e*et|c**o|*de|"
Solution().countAsterisks(s)
# %%
