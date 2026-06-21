from typing import List
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i in range(len(costs)):
            if costs[i] > coins:
                return i
            coins -= costs[i]
        return len(costs)