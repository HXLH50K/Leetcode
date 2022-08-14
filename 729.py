# class MyCalendar:

#     def __init__(self):
#         self.data = [[False] * 10**9]

#     def book(self, start: int, end: int) -> bool:
#         if any(self.data[start:end]):
#             return False
#         else:
#             self.data[start:end] = [True] * (end - start)
#             return True


class MyCalendar:

    def __init__(self):
        self.calendars = []

    def book(self, start: int, end: int) -> bool:
        if not self.calendars:
            self.calendars.append([start, end])
            return True
        for calendar in self.calendars:
            if start < calendar[1] and end > calendar[0]:
                return False
        else:
            self.calendars.append([start, end])
            return True
