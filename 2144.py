from typing import List
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        cost.sort()
        total_cost = 0
        for i in range(n-1, -1, -1):
            if (n - 1 - i) % 3 == 2:
                continue
            total_cost += cost[i]
        return total_cost