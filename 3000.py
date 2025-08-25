class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxx = []
        for l, w in dimensions:
            diag = l**2 + w**2
            if not maxx or diag > maxx[0][0]:
                maxx = [(diag, [l, w])]
                continue
            if diag == maxx[0][0]:
                maxx.append((diag, [l, w]))
                continue
        if len(maxx) == 1:
            return maxx[0][1][0] * maxx[0][1][1]
        maxx.sort(key=lambda x: x[1][0] * x[1][1], reverse=True)
        return maxx[0][1][0] * maxx[0][1][1]
