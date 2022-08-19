# %%
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (ord(coordinates[0]) + int(coordinates[1])) % 2 == 1

a = Solution()
a.squareIsWhite('h3')
# %%
