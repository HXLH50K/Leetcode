# %%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        queue = []
        res = 0
        for r in range(n):
            if s[r] not in queue:
                queue.append(s[r])
                res = max(res, len(queue))
            else:
                while s[r] in queue:
                    queue.pop(0)
                queue.append(s[r])
        res = max(res, len(queue))
        return res


a = Solution()
a.lengthOfLongestSubstring("abcabcbb")

# %%
