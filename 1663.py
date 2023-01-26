# %%
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        k -= n
        num_of_z = k // 25
        mid_char = chr(ord("a") + k - num_of_z * 25) if num_of_z < n else ""
        num_of_a = n - 1 - num_of_z
        return "a" * num_of_a + mid_char + "z" * num_of_z


n = 5
k = 130
Solution().getSmallestString(n, k)

# %%
