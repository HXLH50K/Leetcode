from typing import List
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        for query in queries:
            for word in dictionary:
                if sum(a != b for a, b in zip(query, word)) <= 2:
                    res.append(query)
                    break
        return res