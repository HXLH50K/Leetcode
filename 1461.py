class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        subs = set()
        for i in range(2**k):
            subs.add(bin(i)[2:].zfill(k))
        for i in range(len(s) - k + 1):
            subs.discard(s[i : i + k])
        return len(subs) == 0
