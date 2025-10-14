class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        increase_subs = []
        start = 0
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                end = i - 1
                increase_subs.append((start, end))
                start = i
        increase_subs.append((start, n - 1))

        maxx = 0

        for start, end in increase_subs:
            k = end - start + 1
            maxx = max(maxx, k // 2)

        for i in range(len(increase_subs) - 1):
            first_start, first_end = increase_subs[i]
            second_start, second_end = increase_subs[i + 1]
            k1 = first_end - first_start + 1
            k2 = second_end - second_start + 1
            maxx = max(maxx, min(k1, k2))
        return maxx
