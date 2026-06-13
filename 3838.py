from typing import List
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        word_weights = []
        for word in words:
            weight = sum(weights[ord(char) - ord('a')] for char in word)
            word_weights.append(weight % 26)
        res = ""
        for weight in word_weights:
            res += chr(ord('z')- weight)
        return res