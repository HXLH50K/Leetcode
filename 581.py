# %%
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        left, right = 0, n
        for i in range(n):
            if nums[i:] == sorted_nums[i:]:
                right = i
                break
        for i in range(n, -1, -1):
            if nums[:i] == sorted_nums[:i]:
                left = i
                break
        print(left, right)
        return right - left if right >= left else 0


a = Solution()
a.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
a.findUnsortedSubarray([1, 2, 3, 4])
a.findUnsortedSubarray([2, 1])

# %%
