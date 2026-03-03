# %%
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        S = ["0"]
        while len(S) < n:
            new_S = (
                S[-1] + "1" + "".join("0" if c == "1" else "1" for c in reversed(S[-1]))
            )
            S.append(new_S)
        return S[-1][k - 1]


# %%
