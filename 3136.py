class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        word = word.lower()
        vowels = set("aeiou")
        consonants = set("bcdfghjklmnpqrstvwxyz")
        digits = set("0123456789")
        has_vowel = False
        has_consonant = False
        has_digit = False
        has_illegal_char = False
        for char in word:
            if char in vowels:
                has_vowel = True
            elif char in consonants:
                has_consonant = True
            elif char in digits:
                has_digit = True
            else:
                has_illegal_char = True
                break
        return (has_vowel and has_consonant) and not has_illegal_char
