class Solution:
    def minimumCost(
        self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
    ) -> int:
        if costBoth >= cost1 + cost2:
            return need1 * cost1 + need2 * cost2
        both_needed = min(need1, need2)
        remaining1 = need1 - both_needed
        remaining2 = need2 - both_needed
        return (
            both_needed * costBoth
            + remaining1 * min(cost1, costBoth)
            + remaining2 * min(cost2, costBoth)
        )
