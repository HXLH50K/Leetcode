class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = len(s)
        count = s.count(letter)
        return (count * 100) // n if n > 0 else 0
