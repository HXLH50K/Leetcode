class Solution:
    def doesAliceWin(self, s: str) -> bool:
        if any(c in "aiueo" for c in s):
            return True
        return False
