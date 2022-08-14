#%%
from typing import List


class Solution:

    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        maxx = max(nums)
        bucket = [0] * (maxx + 1)
        for i in range(n):
            bucket[nums[i]] += 1
        j = maxx
        for i in range(1, n, 2):
            while bucket[j] == 0:
                j -= 1
            nums[i] = j
            bucket[j] -= 1
        for i in range(0, n, 2):
            while bucket[j] == 0:
                j -= 1
            nums[i] = j
            bucket[j] -= 1


a = Solution()
nums = [1, 5, 1, 1, 6, 4]
a.wiggleSort(nums)

# %%
