class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m = len(bank)
        n = len(bank[0])
        prev = 0
        res = 0
        for i in range(m):
            count = 0
            for j in range(n):
                if bank[i][j] == "1":
                    count += 1
            if count > 0:
                res += prev * count
                prev = count
        return res
