class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        first_even = not nums[0] & 1
        for i, x in enumerate(nums):
            if (i & 1) == (x & 1) ^ first_even:
                return False
        return True
