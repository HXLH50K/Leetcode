class Solution:
    def binaryGap(self, n: int) -> int:
        n = bin(n)[2:]
        max_gap = 0
        i = 0
        len_n = len(n)
        while i < len_n:
            if n[i] == "1":
                for j in range(i + 1, len(n)):
                    if n[j] == "1":
                        max_gap = max(max_gap, j - i)
                        i = j - 1
                        break
            i += 1

        return max_gap
