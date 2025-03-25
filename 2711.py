class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        answer = [[0] * n for _ in range(m)]

        # Helper function to count unique values in top-left diagonal
        def count_top_left(r: int, c: int) -> int:
            values = set()
            r1, c1 = r - 1, c - 1
            while r1 >= 0 and c1 >= 0:
                values.add(grid[r1][c1])
                r1 -= 1
                c1 -= 1
            return len(values)

        # Helper function to count unique values in bottom-right diagonal
        def count_bottom_right(r: int, c: int) -> int:
            values = set()
            r1, c1 = r + 1, c + 1
            while r1 < m and c1 < n:
                values.add(grid[r1][c1])
                r1 += 1
                c1 += 1
            return len(values)

        # Calculate answer for each cell
        for r in range(m):
            for c in range(n):
                top_left = count_top_left(r, c)
                bottom_right = count_bottom_right(r, c)
                answer[r][c] = abs(top_left - bottom_right)

        return answer
