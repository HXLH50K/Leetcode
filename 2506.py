from collections import defaultdict


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        words = map(lambda x: "".join(sorted(set(x))), words)
        dic = defaultdict(int)
        for word in words:
            dic[word] += 1
        res = 0
        for word in dic:
            res += dic[word] * (dic[word] - 1) // 2
        return res
