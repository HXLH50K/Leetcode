class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        res = 0
        broken = set(brokenLetters)
        for word in text:
            if not any(c in broken for c in word):
                res += 1
        return res
