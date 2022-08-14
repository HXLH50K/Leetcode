class Solution:

    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 1:
            return min(costs[0])
        for i in range(1, n):
            for j in range(3):
                costs[i][j] += min(costs[i - 1][j - 1], costs[i - 1][j - 2])
        return min(costs[-1])