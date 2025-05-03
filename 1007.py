class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        res = -1
        for k in range(1, 7):
            res_top = 0
            res_btm = 0
            cant_flag = False
            for i in range(n):
                if tops[i] != k and bottoms[i] != k:
                    cant_flag = True
                    break
                if tops[i] != k:
                    res_top += 1
                elif bottoms[i] != k:
                    res_btm += 1
            if not cant_flag:
                res = min(res_btm, res_top)

        return res
