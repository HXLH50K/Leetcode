class Solution:
    def isArraySpecial1(self, nums: List[int]) -> bool:
        first_even = not nums[0] & 1
        for i, x in enumerate(nums):
            if (i & 1) == (x & 1) ^ first_even:
                return False
        return True

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ans = []
        for start, end in queries:
            ans.append(self.isArraySpecial1(nums[start : end + 1]))
        return ans
