class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        r = 0
        i = 0
        while True:
            i += 1
            r = (r * 10 + 1) % k
            if r == 0:
                return i
            if i > k:
                return -1
        return -1
