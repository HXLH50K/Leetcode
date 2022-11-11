# %%
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        left = len([x for x in s[: len(s) // 2] if x in vowels])
        right = len([x for x in s[len(s) // 2 :] if x in vowels])
        return left == right
