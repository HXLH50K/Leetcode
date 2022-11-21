# %%
class Solution:
    def dfs(self, a, b):
        if a == 0 and b != 0:
            return 1
        if a == 0 and b == 0:
            return 0.5
        if a != 0 and b == 0:
            return 0
        key = (a, b)
        if key in self.memo and self.memo[key] != 0:
            return self.memo[key]
        prob = 0
        prob += self.dfs(max(0, a - 100), b)
        prob += self.dfs(max(0, a - 75), max(0, b - 25))
        prob += self.dfs(max(0, a - 50), max(0, b - 50))
        prob += self.dfs(max(0, a - 25), max(0, b - 75))
        prob /= 4
        self.memo[key] = prob
        return prob

    def soupServings(self, n: int) -> float:
        if n >= 5000:
            return 1
        self.memo = dict()
        return self.dfs(n, n)
