# %%
from typing import List


class Solution:
    def bt(self, nums, tmp):
        if not nums:
            self.res.append(tmp)
            return
        for i in range(len(nums)):
            self.bt(nums[:i] + nums[i + 1:], tmp + [nums[i]])

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.bt(nums, [])
        return self.res


a = Solution()
a.permute([1, 2, 3])
# %%
