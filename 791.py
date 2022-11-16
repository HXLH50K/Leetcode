# %%
import functools


class Solution:
    def sort(self, a, b):
        return self.order.index(a) - self.order.index(b)

    def customSortString(self, order: str, s: str) -> str:
        s = list(s)
        self.order = list(order)
        s1 = []
        s2 = []
        for x in s:
            if x in self.order:
                s1.append(x)
            else:
                s2.append(x)
        s1.sort(key=functools.cmp_to_key(self.sort))
        return "".join(s1) + "".join(s2)


order = "cba"
s = "abcd"
Solution().customSortString(order, s)

# %%
