class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefixN = [0] * (n + 1)
        suffixY = [0] * (n + 1)
        for i in range(1, n + 1):
            prefixN[i] = prefixN[i - 1] + (1 if customers[i - 1] == "N" else 0)
        for i in range(n - 1, -1, -1):
            suffixY[i] = suffixY[i + 1] + (1 if customers[i] == "Y" else 0)
        res = 0
        minn = float("inf")
        for j in range(n + 1):
            score = prefixN[j] + suffixY[j]
            if score < minn:
                minn = score
                res = j
        return res
