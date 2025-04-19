from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def binary_search_left(arr, target, left):
            """Find leftmost position where arr[pos] >= target"""
            right = len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left

        def binary_search_right(arr, target, left):
            """Find rightmost position where arr[pos] <= target"""
            right = len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left - 1

        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n - 1):
            # For nums[i], find j where lower <= nums[i] + nums[j] <= upper
            # That is: lower - nums[i] <= nums[j] <= upper - nums[i]
            left_bound = lower - nums[i]
            right_bound = upper - nums[i]

            # Find first index where nums[j] >= left_bound
            left_pos = binary_search_left(nums, left_bound, i + 1)
            if left_pos >= n:
                continue

            # Find last index where nums[j] <= right_bound
            right_pos = binary_search_right(nums, right_bound, left_pos)
            if right_pos >= n:
                right_pos = n - 1
            if right_pos < left_pos:
                continue

            count += right_pos - left_pos + 1

        return count
