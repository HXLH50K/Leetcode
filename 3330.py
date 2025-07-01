class Solution:
    def possibleStringCount(self, word: str) -> int:
        i = j = 0
        n = len(word)
        cnt = []
        while i < n:
            j = i + 1
            while j < n and word[j] == word[i]:
                j += 1
            cnt.append(j - i)
            i = j
        return sum(cnt) + 1 - len(cnt)
