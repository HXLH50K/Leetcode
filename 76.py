# %%
from collections import Counter, defaultdict


class Solution:
    def isIn(self, a, b):
        flag = True
        for x in b.keys():
            flag = flag and x in a.keys() and b[x] <= a[x]
            if flag == False:
                break
        return flag

    def minWindow(self, s: str, t: str) -> str:
        l = r = 0
        ans = ""
        minn = float("inf")
        s_dic = defaultdict(lambda: 0)
        t_dic = Counter(t)
        while r <= len(s):
            while not self.isIn(s_dic, t_dic) and r < len(s):
                s_dic[s[r]] += 1
                r += 1
            while self.isIn(s_dic, t_dic):
                tmp = r - l
                if minn > tmp:
                    minn = tmp
                    ans = s[l:r]
                s_dic[s[l]] -= 1
                l += 1
            if r == len(s):
                break
        return ans


a = Solution()
print(a.minWindow(s="ADOBECODEBANC", t="ABC"))
# print(a.minWindow(s="a", t="aa"))
# %%
