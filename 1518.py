class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        now = numBottles
        empty = 0
        while now > 0:
            res += now
            empty += now
            now = empty // numExchange
            empty = empty % numExchange
        return res
