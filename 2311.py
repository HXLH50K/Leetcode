# %%
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        k = bin(k)[2:]
        l = len(s) - len(k)

        if l < 0:
            return len(s)

        while l >= 0 and int(s[l:l+len(k)]) > int(k):
            l -= 1
        if l < 0:
            return len(k) - 1

        return len(k) + s[:l].count('0')


a = Solution()
s = "0"
k = 112
a.longestSubsequence(s, k)


# %%
