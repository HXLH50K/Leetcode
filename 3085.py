# %%
from collections import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = Counter(word)
        ans = float("inf")
        freqs = sorted(cnt.values())
        n = len(freqs)
        for i, freq in enumerate(freqs):
            an = sum(freqs[:i])
            for j in range(i + 1, n):
                if freqs[j] > freq + k:
                    an += freqs[j] - (freq + k)
            ans = min(ans, an)
        return ans


word = "aabcaba"
k = 0
Solution().minimumDeletions(word, k)  # Example usage
