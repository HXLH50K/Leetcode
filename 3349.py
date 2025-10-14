class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        increase_subs = []
        start = 0
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                end = i - 1
                increase_subs.append((start, end))
                start = i
        increase_subs.append((start, n - 1))

        for start, end in increase_subs:
            if end - start + 1 >= 2 * k:
                return True

        for i in range(len(increase_subs) - 1):
            first_start, first_end = increase_subs[i]
            second_start, second_end = increase_subs[i + 1]
            if first_end - first_start + 1 >= k and second_end - second_start + 1 >= k:
                return True
        return False
