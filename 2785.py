class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        s = list(s)
        for c in s:
            if c in "aeiouAEIOU":
                vowels.append(c)
        vowels.sort()
        j = 0
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                s[i] = vowels[j]
                j += 1
        return "".join(s)
