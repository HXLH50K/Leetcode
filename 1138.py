# %%
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = {
            "a": [0, 0],
            "b": [0, 1],
            "c": [0, 2],
            "d": [0, 3],
            "e": [0, 4],
            "f": [1, 0],
            "g": [1, 1],
            "h": [1, 2],
            "i": [1, 3],
            "j": [1, 4],
            "k": [2, 0],
            "l": [2, 1],
            "m": [2, 2],
            "n": [2, 3],
            "o": [2, 4],
            "p": [3, 0],
            "q": [3, 1],
            "r": [3, 2],
            "s": [3, 3],
            "t": [3, 4],
            "u": [4, 0],
            "v": [4, 1],
            "w": [4, 2],
            "x": [4, 3],
            "y": [4, 4],
            "z": [5, 0],
        }
        c = target[0]
        res = "D" * board[c][0] + "R" * board[c][1] + "!"
        for i in range(1, len(target)):
            now_z_flag = prev_z_flag = False
            now_c = target[i]
            prev_c = target[i - 1]
            if now_c == "z":
                now_c = "u"
                now_z_flag = True
            if prev_c == "z":
                prev_c = "u"
                prev_z_flag = True
            if prev_z_flag and now_z_flag:
                res += "!"
                continue
            now_loc = board[now_c]
            prev_loc = board[prev_c]
            re = "U" if prev_z_flag else ""
            re += (
                "D" * max(0, now_loc[0] - prev_loc[0])
                + "U" * max(0, prev_loc[0] - now_loc[0])
                + "R" * max(0, now_loc[1] - prev_loc[1])
                + "L" * max(0, prev_loc[1] - now_loc[1])
            )
            re += "D" if now_z_flag else ""
            re += "!"
            res += re

        return res


target = "zz"
Solution().alphabetBoardPath(target)

# %%
