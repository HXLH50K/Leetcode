class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        if n == 1:
            return True
        if bits[-2] == 0:
            return True
        count_1 = 0
        for i in range(n - 2, -1, -1):
            if bits[i] == 1:
                count_1 += 1
            else:
                break
        return count_1 % 2 == 0
