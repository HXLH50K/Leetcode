# %%
from typing import List

# %%
# class GraphNode:

#     def __init__(self, val):
#         self.val = val
#         self.near = []
#         self.visited = False

# class Solution:

#     def __init__(self):
#         self.re = 0
#         self.res = 0

#     def gcd(self, a, b):
#         while (b != 0):
#             if a % b == 0:
#                 return b
#             else:
#                 return self.gcd(b, a % b)

#     def dfs(self, node):
#         if node.visited:
#             return
#         node.visited = True
#         self.re += 1
#         for x in node.near:
#             self.dfs(x)

#     def largestComponentSize(self, nums: List[int]) -> int:
#         for i in range(len(nums)):
#             nums[i] = GraphNode(nums[i])
#         for i in range(len(nums) - 1):
#             for j in range(i + 1, len(nums)):
#                 if self.gcd(nums[i].val, nums[j].val) > 1:
#                     nums[i].near.append(nums[j])
#                     nums[j].near.append(nums[i])
#         self.res = 0
#         for node in nums:
#             self.re = 0
#             self.dfs(node)
#             self.res = max(self.res, self.re)
#         return self.res


# %%
class Solution:

    def __init__(self):
        self.dict = {
            2: set(),
            3: set(),
            5: set(),
            7: set(),
            11: set(),
            13: set(),
            17: set()
        }
        self.newdict = {}

    def largestComponentSize(self, nums: List[int]) -> int:
        for num in nums:
            for k in self.dict:
                if num % k == 0:
                    self.dict[k].add(num)
        res = 0
        for k in self.dict:
            res = max(res, len(self.dict[k]))
        return res


a = Solution()
nums = [20, 50, 9, 63]
a.largestComponentSize(nums)
# %%
