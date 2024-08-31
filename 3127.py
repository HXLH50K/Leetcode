class Solution:
    def canMakeSquare22(self, grid: List[List[str]]) -> bool:
        flattened_grid = [cell for row in grid for cell in row]
        count_W = flattened_grid.count("W")
        count_B = flattened_grid.count("B")
        return count_W <= 1 or count_B <= 1

    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(2):
            for j in range(2):
                if self.canMakeSquare22([row[j : j + 2] for row in grid[i : i + 2]]):
                    return True
        return False
