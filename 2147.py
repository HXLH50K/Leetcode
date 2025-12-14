# %%
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        cnt_S = corridor.count("S")
        if cnt_S & 1 != 0 or cnt_S == 0:
            return 0

        corridor = corridor.strip("P")
        seat_stack = 0
        cnt_plant = [0]

        for c in corridor:
            if c == "S":
                if seat_stack == 0:
                    seat_stack += 1
                else:
                    seat_stack = 0
                    cnt_plant.append(0)
            elif c == "P":
                if seat_stack == 0:
                    cnt_plant[-1] += 1

        res = 1
        MOD = 10**9 + 7
        for cnt in cnt_plant:
            if cnt == 0:
                continue
            res = (res * (cnt + 1)) % MOD

        return res


corridor = "S"
Solution().numberOfWays(corridor)

# %%
