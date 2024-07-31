class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        xs = [point[0] for point in points]
        xs.sort()
        res = 0
        n = len(xs)
        rec_left = 0
        for i in range(n):
            if xs[i] - xs[rec_left] > w:
                res += 1
                rec_left = i
        return res + 1
