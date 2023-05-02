# %%
class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        day_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        arrive_month_alice, arrive_day_alice = map(int, arriveAlice.split("-"))
        leave_month_alice, leave_day_alice = map(int, leaveAlice.split("-"))
        arrive_month_bob, arrive_day_bob = map(int, arriveBob.split("-"))
        leave_month_bob, leave_day_bob = map(int, leaveBob.split("-"))
        arrive_data_alice = (
            sum(day_of_month[: arrive_month_alice - 1]) + arrive_day_alice
        )
        leave_data_alice = sum(day_of_month[: leave_month_alice - 1]) + leave_day_alice
        arrive_data_bob = sum(day_of_month[: arrive_month_bob - 1]) + arrive_day_bob
        leave_data_bob = sum(day_of_month[: leave_month_bob - 1]) + leave_day_bob
        if arrive_data_alice > leave_data_bob or arrive_data_bob > leave_data_alice:
            return 0
        else:
            return (
                min(leave_data_alice, leave_data_bob)
                - max(arrive_data_alice, arrive_data_bob)
                + 1
            )


arriveAlice = "08-15"
leaveAlice = "08-18"
arriveBob = "08-16"
leaveBob = "08-19"
Solution().countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob)

# %%
