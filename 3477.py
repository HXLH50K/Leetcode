class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for fruit in fruits:
            for i, basket in enumerate(baskets):
                if basket >= fruit:
                    del baskets[i]
                    break
        return len(baskets)
