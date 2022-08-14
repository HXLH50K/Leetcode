# %%
from typing import List


class Solution:

    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))
        res = []
        for i in range(len(words) - 1):
            for j in range(len(words) - 1, i, -1):
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res
