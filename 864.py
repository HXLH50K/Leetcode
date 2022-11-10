# %%
from typing import List


class State:
    def __init__(self, x, y, key):
        self.x = x
        self.y = y
        self.key = key


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m = len(grid)
        n = len(grid[0])
        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        keycnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    start = State(i, j, 0)
                if "a" <= grid[i][j] <= "f":
                    keycnt += 1

        q = [start]
        allkey = (1 << keycnt) - 1
        visisted = [
            [[False for _ in range(allkey + 1)] for _ in range(n)] for _ in range(m)
        ]
        step = 0
        while q:
            l = len(q)
            for i in range(l):
                curr = q.pop(0)
                if curr.key == allkey:
                    return step

                for move in moves:
                    x, y = curr.x + move[0], curr.y + move[1]
                    if x < 0 or y < 0 or x >= m or y >= n:
                        continue
                    c = grid[x][y]
                    key = curr.key
                    if c == "#":
                        continue
                    if "A" <= c <= "F" and (key >> (ord(c) - ord("A")) & 1) == 0:
                        continue
                    if "a" <= c <= "f":
                        key |= 1 << (ord(c) - ord("a"))
                    if visisted[x][y][key]:
                        continue
                    visisted[x][y][key] = True
                    q.append(State(x, y, key))
            step += 1
        return -1
