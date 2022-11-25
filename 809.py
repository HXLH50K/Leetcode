class Solution:
    def isExpressived(self, s, word):
        i = j = 0
        while i < len(s) and j < len(word):
            if s[i] != word[j]:
                return False
            c = s[i]

            cnts = 0
            while i < len(s) and s[i] == c:
                i += 1
                cnts += 1

            cntw = 0
            while j < len(word) and word[j] == c:
                j += 1
                cntw += 1

            if cnts < cntw:
                return False
            if cnts > cntw and cnts < 3:
                return False
        return i == len(s) and j == len(word)

    def expressiveWords(self, s: str, words: List[str]) -> int:
        res = 0
        for word in words:
            res += self.isExpressived(s, word)
        return res
