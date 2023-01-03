#%%
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split()
        last = -float("inf")
        for x in s:
            try:
                now = int(x)
                if now <= last:
                    return False
                last = now
            except:
                pass
        return True


Solution().areNumbersAscending("1 box has 1 blue 4 red 6 green and 12 yellow marbles")

# %%
