# %%
class Solution:

    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        n = len(num)
        i = 0
        while i < n:
            maxx = max(num[i:])
            if num[i] == maxx:
                i += 1
                continue
            j = num[i:].index(maxx) + i
            num[i], num[j] = num[j], num[i]
            break
        return int("".join(num))


a = Solution()
a.maximumSwap(98368)
# %%
