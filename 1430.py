class Solution:

    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        summ = sum(nums)
        res_sum = 0
        for i, x in enumerate(nums):
            res_sum += x
            if res_sum > summ - res_sum:
                break
        return nums[:i + 1]
