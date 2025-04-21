class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        hidden = [0]
        minn = 0
        maxx = 0
        for x in differences:
            hidden.append(hidden[-1] + x)
            minn = min(hidden[-1], minn)
            maxx = max(hidden[-1], maxx)
        maxx += lower - minn
        return max(upper - maxx + 1, 0)
