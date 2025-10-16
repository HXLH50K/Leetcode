from collections import Counter


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        nums = [num % value for num in nums]
        count = Counter(nums)
        for i in range(value):
            if i not in count:
                return i
        # find the min frequency and return the index + 1
        min_freq = min(count.values())
        for i in range(value):
            if count[i] == min_freq:
                return i + min_freq * value
