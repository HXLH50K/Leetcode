#%%
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        cnt = 0
        while nums[-1] != 0:
            for i in range(n):
                if nums[i] % 2 != 0:
                    nums[i] -= 1
                    cnt += 1
                nums[i] /= 2
            cnt += 1
            # for i in range(n):
            #     nums[i] /= 2
            # cnt += 1
            print(nums)
        return max(0, cnt - 1)


a = Solution()
print(a.minOperations([1, 5]))
# %%
print(a.minOperations([2, 2]))
# %%
