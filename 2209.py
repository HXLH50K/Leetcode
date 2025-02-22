class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        # dp[i][j] represents minimum number of white tiles uncovered
        # when considering first i tiles with j carpets available
        dp = {}

        def solve(pos, carpets):
            if carpets < 0:
                return float("inf")
            if pos >= n:
                return 0

            if (pos, carpets) in dp:
                return dp[(pos, carpets)]

            # Don't place carpet here
            dont_place = (1 if floor[pos] == "1" else 0) + solve(pos + 1, carpets)

            # Place carpet here
            place = solve(pos + carpetLen, carpets - 1)

            dp[(pos, carpets)] = min(dont_place, place)
            return dp[(pos, carpets)]

        return solve(0, numCarpets)
