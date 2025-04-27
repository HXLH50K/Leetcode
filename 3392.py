class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        summ = nums[0] + nums[1]
        res = 0
        for i in range(2, len(nums)):
            summ += nums[i]
            if summ == 1.5 * nums[i - 1]:
                res += 1
            summ -= nums[i - 2]
        return res
