class Solution:
    def maxOperations(self, s: str) -> int:
        ones = []
        n = len(s)
        # use double pointer to find the groups of '1's
        i = 0
        while i < n:
            if s[i] == "1":
                j = i
                while j < n and s[j] == "1":
                    j += 1
                ones.append(j - i)
                i = j
            else:
                i += 1
        if s[n - 1] == "1":
            ones.pop(-1)  # remove the last group if it ends with '1'
        res = 0
        m = len(ones)
        for i in range(m):
            res += ones[i] * (m - i)
        return res
