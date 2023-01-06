# %%
class Solution:
    def countEven(self, num: int) -> int:
        res = []
        for i in range(1, 1001):
            x = list(map(int, [c for c in str(i)]))
            if sum(x) % 2 == 0:
                res.append(i)
        return res
        return len([x for x in res if x <= num])


Solution().countEven(1)

# %%
