# %%
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        l = [0] * n
        r = [n] * n
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                r[stack.pop()] = i
            stack.append(i)
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                l[stack.pop()] = i + 1
            stack.append(i)
        res = 0
        for i in range(n):
            res = max(res, heights[i] * (r[i] - l[i]))
        return res


a = Solution()
a.largestRectangleArea([2, 1, 5, 6, 2, 3])

# %%
