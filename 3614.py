class Solution:
    def processStr(self, s: str, k: int) -> str:
        res = ""
        for c in s:
            if c == "*":
                if len(res) > 0:
                    res = res[:-1]
                continue
            if c == "#":
                res = res + res
                continue
            if c == "%":
                res = res[::-1]
                continue
            res = res + c
        return res[k] if k < len(res) else "."