# %%
from typing import List


class Solution:
    def oddString(self, words: List[str]):
        words_offset = []
        for i in range(len(words)):
            diff = ord(words[i][0]) - ord("a")
            re = "".join([chr(ord(x) - diff) for x in words[i]])
            words_offset.append(re)
        for i in range(len(words) - 1):
            if words_offset[i] == words_offset[i + 1]:
                continue
            return (
                words[i] if words_offset[i - 1] == words_offset[i + 1] else words[i + 1]
            )


words = ["aaa","bob","ccc","ddd"]
Solution().oddString(words)

# %%
