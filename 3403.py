# %%
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        max_locs = [i for i in range(n) if word[i] == max(word)]
        max_len = n - numFriends + 1
        res = ""
        for loc in max_locs:
            res = max(res, word[loc : min(n, loc + max_len)])
        return res


word = "dbca"
numFriends = 2
Solution().answerString(word, numFriends)

# %%
