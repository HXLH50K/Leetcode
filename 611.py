# %%
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        cnt = 0
        loc = 0
        for i, x in enumerate(nums):
            if x != 0:
                loc = i
                break
        nums = nums[i:]
        n = len(nums)
        for i in range(n - 1, 1, -1):
            j, k = 0, i - 1
            while j < k:
                if nums[i] < nums[j] + nums[k]:
                    cnt += k - j
                    k -= 1
                else:
                    j += 1
        return cnt


a = Solution()
a.triangleNumber([2, 2, 3, 4])

# %%
