# %%
from typing import List


class Solution:

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        sentence = sentence.split(" ")
        for i, word in enumerate(sentence):
            for root in dictionary:
                if word.startswith(root):
                    sentence[i] = root
                    break
        res = " ".join(sentence)
        return res


a = Solution()
dictionary = ["a", "b", "c"]
sentence = "aadsfasf absbs bbab cadsfafs"
a.replaceWords(dictionary, sentence)

# %%
