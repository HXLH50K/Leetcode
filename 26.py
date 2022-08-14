# %%
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        i = 0
        j = 1
        while j<len(nums):
            j = i + 1
            while nums[i] >= nums[j] and j<len(nums)-1:
                j+=1
            i+=1
            nums[i] = nums[j]
            print(i,j)
        return len(nums)

def main():
    nums = [1,1,2]
    ret = Solution().removeDuplicates(nums)
    out = str(ret)
    print(out)

if __name__ == '__main__':
    main()
# %%
