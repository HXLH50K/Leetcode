# %%
from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        origin = sorted(nums)
        flag = origin[0]

        try:
            bias = nums.index(flag)
        except:
            return False

        if bias == 0:
            for i in range(n - 1, -1, -1):
                if nums[i] != flag:
                    bias = (i + 1) % n
                    break
        for i in range(n):
            if origin[i] != nums[(i + bias) % n]:
                return False
        return True
