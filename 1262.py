class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float("-inf"), float("-inf")]
        for num in nums:
            ndp = dp[:]
            for i in range(3):
                ndp[(i + num) % 3] = max(ndp[(i + num) % 3], dp[i] + num)
            dp = ndp
        return dp[0]
