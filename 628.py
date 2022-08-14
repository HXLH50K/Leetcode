# %%
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a = [float('-inf') for _ in range(3)]
        b = [float('inf') for _ in range(2)]
        for x in nums:
            if x > min(a):
                a.append(x)
                a.sort(reverse=True)
                print(a)
                a = a[:3]
            if x < max(b):
                b.append(x)
                b.sort()
                b = b[:2]
        print(a, b)
        return max(b[0] * b[1] * a[0], a[0] * a[1] * a[2])


a = Solution()
a.maximumProduct([1, 2, 3])
# %%
