class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:

        diff_1 = abs(x - z)
        diff_2 = abs(y - z)
        if diff_1 == diff_2:
            return 0
        if diff_1 < diff_2:
            return 1
        return 2
