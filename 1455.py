# %%
class Solution:

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        res = -1
        for i, x in enumerate(sentence.split(" ")):
            if x.startswith(searchWord):
                res = i + 1
                break
        return res


a = Solution()
sentence = "i love eating burger"
searchWord = "burg"
a.isPrefixOfWord(sentence, searchWord)
# %%
