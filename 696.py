class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        n = len(s)
        cur_cnt = 0
        for i in range(n - 1):
            cur_cnt += 1
            if s[i] != s[i + 1]:
                groups.append(cur_cnt)
                cur_cnt = 0
        cur_cnt += 1
        if cur_cnt > 0:
            groups.append(cur_cnt)
        res = 0
        n = len(groups)
        for i in range(n - 1):
            res += min(groups[i], groups[i + 1])
        return res
