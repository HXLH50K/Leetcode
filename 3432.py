class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        summ = sum(nums)
        sum_l = 0
        n = len(nums)
        res = 0
        for i in range(n - 1):
            sum_l += nums[i]
            sum_r = summ - sum_l
            if (sum_r - sum_l) & 1 == 0:
                res += 1
        return res
