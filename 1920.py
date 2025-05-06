class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            ans.append(nums[x])
        return ans
