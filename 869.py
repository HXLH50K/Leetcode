from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        targets = []
        i = 0
        while True:
            num = 2**i
            i += 1
            if num > 1e9:
                break
            targets.append(Counter(list(str(num))))
        n = Counter(list(str(n)))
        for num in targets:
            if n == num:
                return True
        return False
