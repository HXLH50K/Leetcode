class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        points = []
        for i in range(len(possible)):
            point = -1 if possible[i] == 0 else 1
            points.append(point)
        l_sum = 0
        summ = sum(points)
        for i in range(len(points) - 1):
            l_sum += points[i]
            if l_sum > summ - l_sum:
                return i + 1
        return -1
