import numpy as np


class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = np.zeros((rows, 26), dtype=int)

    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0]) - ord("A")
        row = int(cell[1:]) - 1
        self.sheet[row, col] = value

    def resetCell(self, cell: str) -> None:
        col = ord(cell[0]) - ord("A")
        row = int(cell[1:]) - 1
        self.sheet[row, col] = 0

    def getValue(self, formula: str) -> int:
        formula = formula[1:]  # remove "="
        a, b = formula.split("+")
        res = 0
        if a.isdigit():
            res += int(a)
        else:
            col = ord(a[0]) - ord("A")
            row = int(a[1:]) - 1
            res += self.sheet[row, col]
        if b.isdigit():
            res += int(b)
        else:
            col = ord(b[0]) - ord("A")
            row = int(b[1:]) - 1
            res += self.sheet[row, col]
        return int(res)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
