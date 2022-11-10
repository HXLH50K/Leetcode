# %%
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # nums = [i for i in range(n)]
        # i = 0
        # while n > 1:
        #     i = (i + (m - 1)) % n
        #     del nums[i]
        #     n -= 1
        # return nums
        res = 0
        for i in range(1, n + 1):
            res = (res + m) % i
        return res


a = Solution()
a.lastRemaining(10, 17)

# %%
