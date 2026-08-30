# %%
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        l = 0
        while s[l] == 0:
            l += 1
        r = l
        one_count = 0
        candidates = []
        while r < n:
            if s[r] == 1:
                one_count += 1
            if one_count == k:
                candidates.append(s[l : r + 1])
                l += 1
                while s[l] == 0:
                    l += 1
            r += 1
        print(candidates)
        return ""


s = "100011001"
k = 3
solution = Solution()
solution.shortestBeautifulSubstring(s, k)
