# %%
class Solution:
    def findSubstring(self, s, words):
        from collections import Counter
        import re
        if not s or not words:
            return []
        word_num = len(words)
        one_word_len = len(words[0])
        words = Counter(words)
        n = len(s)
        res = []
        for i in range(n - word_num * one_word_len + 1):
            temp = re.findall(r"\w{%s}" % one_word_len,
                              s[i:i + word_num * one_word_len])
            print(temp)
            if Counter(temp) == words:
                res.append(i)
        return res


a = Solution()
a.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"])

# %%
