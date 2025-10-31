from collections import Counter


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        sneaky_numbers = [num for num, freq in count.items() if freq != 1]
        return sorted(sneaky_numbers)
