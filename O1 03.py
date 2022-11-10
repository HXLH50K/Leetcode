# %%
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
            elif nums[i] == nums[nums[i]]:
                return nums[i]
            else:
                # a = nums[i]
                # b = nums[nums[i]]
                # nums[i], nums[a] = b, a
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]


a = Solution()
a.findRepeatNumber([2, 3, 1, 0, 2, 5, 3])

# %%
