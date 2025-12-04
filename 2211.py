class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        left, right = 0, n - 1
        while left < n and directions[left] == "L":
            left += 1
        while right >= 0 and directions[right] == "R":
            right -= 1
        return right - left + 1 - directions.count("S") if right >= left else 0
