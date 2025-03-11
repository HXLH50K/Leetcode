class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        res = 0
        for i in range(len(str(num)) - k + 1):
            a = int(str(num)[i : i + k])
            if a == 0:
                continue
            if num % a == 0:
                res += 1
        return res
