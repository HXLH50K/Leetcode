class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7

        total = 0
        for week in range(weeks + 1):
            monday_amount = 1 + week
            if week == weeks:
                for day in range(days):
                    total += monday_amount + day
            else:
                for day in range(7):
                    total += monday_amount + day
        return total
