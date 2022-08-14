# %%
class Solution:

    def cacl(self, arr):
        x = 0
        common = 0
        for item in arr:
            try:
                common += int(item)
            except:
                if item == "x":
                    item = "1x"
                elif item == "-x":
                    item = "-1x"
                x += int(item[:-1])
        return x, common

    def solveEquation(self, equation: str) -> str:
        equation = equation.replace("-", "+-")
        left, right = equation.split("=")
        left = list(filter(None, left.split("+")))
        right = list(filter(None, right.split("+")))
        left_x, left_common = self.cacl(left)
        right_x, right_common = self.cacl(right)

        if left_x == right_x and left_common == right_common:
            return "Infinite solutions"
        if left_x == right_x and left_common != right_common:
            return "No solution"
        return f"x={str(int((right_common - left_common) / (left_x - right_x)))}"


a = Solution()
equation = "-x=-0"
a.solveEquation(equation)
# %%
