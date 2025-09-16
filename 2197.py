class Solution:
    def findGCD(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def findLCM(self, a: int, b: int) -> int:
        return a * b // self.findGCD(a, b)

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            while stack and self.findGCD(stack[-1], num) > 1:
                num = self.findLCM(stack.pop(), num)
            stack.append(num)
        return stack
