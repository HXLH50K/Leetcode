# %%
from itertools import permutations


class Solution:

    def nextGreaterElement(self, n: int) -> int:
        n = str(n)
        perms = [
            int("".join(x)) for x in permutations(n, len(n))
            if 2**31 > int("".join(x)) > int(n)
        ]
        return min(perms) if perms and min(perms) < 2**31 else -1


a = Solution()
a.nextGreaterElement(2147483647)
# %%
