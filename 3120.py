class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word = set(word)
        count = 0
        for low_alpha in "abcdefghijklmnopqrstuvwxyz":
            if low_alpha in word and low_alpha.upper() in word:
                count += 1
        return count