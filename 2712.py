class Solution:
    def minimumCost(self, s: str) -> int:
        cost_left = []
        cost_right = []
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                cost_left.append(i)
                cost_right.append(len(s) - i)
        return sum(min(a, b) for a, b in zip(cost_left, cost_right))
