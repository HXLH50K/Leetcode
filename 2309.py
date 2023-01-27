# %%
class Solution:
    def greatestLetter(self, s: str) -> str:
        sset = set(s)
        for i in range(25, -1, -1):
            if chr(ord("A") + i) in sset and chr(ord("a") + i) in sset:
                return chr(ord("A") + i)
        return ""


s = "nzmguNAEtJHkQaWDVSKxRCUivXpGLBcsjeobYPFwTZqrhlyOIfdM"
Solution().greatestLetter(s)

# %%
