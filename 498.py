from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        red_digs = defaultdict(list)
        yellow_digs = defaultdict(list)
        for i in range(m):
            for j in range(n):
                if (i + j) % 2 == 0:
                    red_digs[i + j].append((i, mat[i][j]))
                else:
                    yellow_digs[i + j].append((j, mat[i][j]))
        for key in red_digs:
            red_digs[key].sort(reverse=True, key=lambda x: x[0])
        for key in yellow_digs:
            yellow_digs[key].sort(reverse=True, key=lambda x: x[0])
        digs = dict()
        # merge two dicts
        for key in red_digs:
            digs[key] = red_digs[key]
        for key in yellow_digs:
            digs[key] = yellow_digs[key]
        digs = dict()
        # merge two dicts
        for key in red_digs:
            digs[key] = red_digs[key]
        for key in yellow_digs:
            digs[key] = yellow_digs[key]
        result = []
        for _, v in sorted(digs.items()):
            val = [x[1] for x in v]
            result.extend(val)
        return result
