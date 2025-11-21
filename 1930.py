class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        res = 0
        i = 0
        seen = set()
        for i in range(n - 1):
            ch = s[i]
            if ch in seen:
                continue
            seen.add(ch)
            j = n - 1
            while j > i:
                if s[j] == ch:
                    break
                j -= 1
            res += len(set(s[i + 1 : j]))
        return res
