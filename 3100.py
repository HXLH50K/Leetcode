class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full_bottles = numBottles
        empty_bottles = 0
        total_drunk = 0
        while full_bottles > 0:
            total_drunk += full_bottles
            empty_bottles += full_bottles
            full_bottles = 0
            while empty_bottles >= numExchange:
                empty_bottles -= numExchange
                full_bottles += 1
                numExchange += 1
        return total_drunk