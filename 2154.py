class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num_set = set(nums)
        while original <= 1000:
            if original in num_set:
                original *= 2
            else:
                return original
        return original
