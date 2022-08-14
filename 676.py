#%%
from typing import List


class MagicDictionary:

    def __init__(self):
        self.dictionary = dict()

    def buildDict(self, dictionary: List[str]) -> None:
        for x in dictionary:
            if len(x) not in self.dictionary:
                self.dictionary[len(x)] = [x]
            else:
                self.dictionary[len(x)].append(x)

    def search(self, searchWord: str) -> bool:
        try:
            candidates = self.dictionary[len(searchWord)]
        except KeyError:
            return False

        for x in candidates:
            assert len(x) == len(searchWord)
            miss_char = 0
            for i in range(len(x)):
                if x[i] != searchWord[i]:
                    miss_char += 1
                if miss_char > 1:
                    break
            if miss_char == 1:
                return True
        return False


magicDictionary = MagicDictionary()
magicDictionary.buildDict(["hello", "hallo", "leetcode"])
magicDictionary.search("hello")
# %%
