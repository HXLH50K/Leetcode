class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if max(nums) >= sum(nums) / 2:
            return "none"
        a, b, c = nums
        if a == b and b == c:
            return "equilateral"
        if a == b or b == c or a == c:
            return "isosceles"
        return "scalene"
