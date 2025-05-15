class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        flag_a = False
        flag_b = True
        res_a = []
        res_b = []
        n = len(words)
        for i in range(n):
            if bool(groups[i]) == flag_a:
                res_a.append(words[i])
                flag_a = not flag_a
            if bool(groups[i]) == flag_b:
                res_b.append(words[i])
                flag_b = not flag_b
        return res_a if len(res_a) > len(res_b) else res_b
