class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        chars = [0] * 26
        for c in s:
            chars[ord(c) - ord("a")] += 1
        for _ in range(t):
            new_chars = [0] * 26
            for i in range(26):
                if i != 25:
                    new_chars[i + 1] = chars[i]
                else:
                    new_chars[0] += chars[i]
                    new_chars[1] += chars[i]
            chars = [x % MOD for x in new_chars]
        return sum(chars) % MOD
