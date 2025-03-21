class Solution:
    def maximumOr(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # 计算前缀或和后缀或
        prefix = [0] * (n + 1)  # prefix[i]表示nums[0]到nums[i-1]的或值
        suffix = [0] * (n + 1)  # suffix[i]表示nums[i+1]到nums[n-1]的或值

        # 计算前缀或
        for i in range(n):
            prefix[i + 1] = prefix[i] | nums[i]

        # 计算后缀或
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] | nums[i]

        ans = 0
        # 尝试将每个数字左移k位
        for i in range(n):
            # 当前数字左移k位后的值
            shifted = nums[i] << k
            # 其余数字保持不变
            current = prefix[i] | shifted | suffix[i + 1]
            ans = max(ans, current)

        return ans
