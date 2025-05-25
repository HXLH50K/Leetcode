# %%
from typing import List
from collections import defaultdict


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dic = defaultdict(int)
        res = 0
        for word in words:
            if dic[word[::-1]] > 0:
                res += 2
                dic[word[::-1]] -= 1
            else:
                dic[word] += 1
        for word, cnt in dic.items():
            if cnt > 0 and word[0] == word[1]:
                res += 1
                break

        return res * 2


words = ["lc", "cl", "gg"]
Solution().longestPalindrome(words)
