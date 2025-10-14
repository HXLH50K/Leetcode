class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        for i in range(n):
            sorted_i = sorted(words[i])
            for j in range(i + 1, n):
                sorted_j = sorted(words[j])
                if sorted_i == sorted_j:
                    words[j] = ""
                    continue
                else:
                    break
        return [word for word in words if word != ""]
