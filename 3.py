# %%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        i = 0
        j = 1
        while j <= len(s):
            if len(s[i:j]) == len(set(s[i:j])):
                res = max(res, j - i)
                j += 1
            else:
                i += 1
        return res


a = Solution()
a.lengthOfLongestSubstring("abcabcbb")
# %%
