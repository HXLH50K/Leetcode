class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(s)
        res = ""
        for i in range(n - 1, -1, -1):
            res = s[i] + res
            if i == spaces[-1]:
                spaces.pop(-1)
                res = " " + res
        return res
