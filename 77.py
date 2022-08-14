# %%
from typing import List


class Solution:
    def dfs(self, n, k, i):
        if len(self.path) == k:
            self.res.append(self.path.copy())
            return
        for x in range(i, n):
            self.path.append(x + 1)
            self.dfs(n, k, x + 1)
            self.path.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.path = []
        self.dfs(n, k, 0)


# class Solution:
#     def dfs(self, n, k):
#         if len(self.path) == k:
#             self.res.append(self.path.copy())
#             return
#         for x in range(n, 0, -1):
#             self.path.append(x)
#             self.dfs(n - 1, k)
#             self.path.pop()

#     def combine(self, n: int, k: int) -> List[List[int]]:
#         self.res = []
#         self.path = []
#         self.dfs(n, k)

a = Solution()
a.combine(4, 2)
print(a.res)

# %%
