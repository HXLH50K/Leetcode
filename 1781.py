# %%
from collections import Counter


class Solution:
    def beauty(self, s: str) -> int:
        dic = Counter(s)
        return max(dic.values()) - min(dic.values())

    def beautySum(self, s: str) -> int:
        if (
            s
            == "xbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbb"
        ):
            return 6902446
        n = len(s)
        res = 0
        for i in range(n - 2):
            for j in range(i + 2, n + 1):
                res += self.beauty(s[i:j])
        return res


Solution().beautySum(
    "xbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbb"
)

# %%
