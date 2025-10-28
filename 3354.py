class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        left_sum = []
        right_sum = []
        n = len(nums)
        for i in range(n):
            if i == 0:
                left_sum.append(nums[i])
            else:
                left_sum.append(left_sum[-1] + nums[i])
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                right_sum.append(nums[i])
            else:
                right_sum.append(right_sum[-1] + nums[i])
        right_sum.reverse()
        count = 0
        for i in range(n):
            if nums[i] != 0:
                continue
            if left_sum[i] == right_sum[i]:
                count += 2
            if abs(left_sum[i] - right_sum[i]) == 1:
                count += 1
        return count
